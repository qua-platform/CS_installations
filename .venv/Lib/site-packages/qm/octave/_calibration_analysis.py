import logging
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union, Optional, cast

import numpy as np

from qm.api.v2.job_api import JobApi
from qm.jobs.running_qm_job import RunningQmJob
from qm.octave._calibration_names import SavedVariablesNames as Names

Array = np.typing.NDArray[np.cdouble]


logger = logging.getLogger(__name__)


def _polyfit2d(x: Array, y: Array, z: Array, kx: int = 2, ky: int = 2, order: Optional[int] = None) -> Array:
    """
    Two-dimensional polynomial fitting by least squares.
    Fits the functional form f(x,y) = z.

    Notes
    -----
    Resultant fit can be plotted with:
    np.polynomial.polynomial.polygrid2d(x, y, soln.reshape((kx+1, ky+1)))

    Parameters
    ----------
    x, y: array-like, 1d
        x and y coordinates.
        len(x) mest be z.shape[0] and len(y) must be z.shape[1]
    z: np.ndarray, 2d
        Surface to fit.
    kx, ky: int, default is 3
        Polynomial order in x and y, respectively.
    order: int or None, default is None
        If None, all coefficients up to maximum kx, ky, i.e. up to and including x^kx*y^ky, are considered.
        If int, coefficients up to a maximum of kx+ky <= order are considered.

    Returns
    -------
    Return parameters from np.linalg.lstsq.

    soln: np.ndarray
        Array of polynomial coefficients.
    residuals: np.ndarray
    rank: int
    s: np.ndarray

    """

    # grid coords
    x, y = np.meshgrid(x, y)
    # coefficient array, up to x^kx, y^ky
    coefficients = np.ones((kx + 1, ky + 1))

    # solve array
    a = np.zeros((coefficients.size, x.size))

    # for each coefficient produce array x^i, y^j
    for index, (j, i) in enumerate(np.ndindex(*coefficients.shape)):
        # do not include powers greater than order
        if order is not None and i + j > order:
            arr = np.zeros_like(x)
        else:
            arr = coefficients[i, j] * x**i * y**j
        a[index] = arr.ravel()

    # do least-squares fitting
    return cast(Array, np.linalg.lstsq(a.T, np.ravel(z), rcond=None)[0])


@dataclass
class FitResult:
    pol: Array
    x_min: float
    y_min: float
    theta: float
    pol_: Array


def _paraboloid2d_fit(x: Array, y: Array, z: Array) -> FitResult:
    """
    Two-dimensional paraboloid fitting by least squares.
    Fits the functional form a0 + a1*x + a2*y + a3*x**2 + a4*x*y + a5*y**2 = z.

    Parameters
    ----------
    x, y: array-like, 1d
        x and y coordinates.
        len(x) mest be z.shape[0] and len(y) must be z.shape[1]
    z: np.ndarray, 2d
        Surface to fit.

    Returns
    -------
    A dictionary with the fitted polynom and the axis of the minimal point:

    pol
    x_min
    y_min

    """

    p = _polyfit2d(x, y, z, order=2).take([0, 1, 3, 2, 4, 6])

    theta = np.arctan2(-p[4], p[3] - p[5]) / 2.0
    c = np.cos(theta)
    s = np.sin(theta)

    p_ = (
        np.array(
            [
                [1, 0, 0, 0, 0, 0],  # 1
                [0, c, -s, 0, 0, 0],  # x
                [0, s, c, 0, 0, 0],  # y
                [0, 0, 0, c**2, -c * s, s**2],  # x**2
                [0, 0, 0, 2 * c * s, c**2 - s**2, -2 * c * s],  # x*y
                [0, 0, 0, s**2, c * s, c**2],  # y**2
            ]
        )
        @ p
    )

    x0_ = -p_[1] / (2 * p_[3])
    y0_ = -p_[2] / (2 * p_[5])

    xy_min = np.array([[c, s], [-s, c]]) @ [x0_, y0_]

    return FitResult(pol=p, x_min=xy_min[0], y_min=xy_min[1], theta=theta, pol_=p_)


def _get_reshaped_data(
    job: Union[RunningQmJob, JobApi], n_samples: int, offset: int, count: int, *names: str
) -> Dict[str, Array]:
    data_first = offset * n_samples**2
    data_last = (offset + count) * n_samples**2

    name_to_result_handle = {}
    for name in names:
        result_handle = job.result_handles.get(name)
        assert result_handle is not None
        name_to_result_handle[name] = result_handle
        result_handle.wait_for_values(data_last)

    raw_data = {}
    for name in names:
        result_handle = name_to_result_handle[name]
        raw_data[name] = result_handle.fetch(slice(data_first, data_last), flat_struct=True)

    full_data = {}
    for name, value in raw_data.items():
        full_data[name] = np.array(value).reshape((-1, n_samples, n_samples))

    return full_data


@dataclass
class CorrectionsDebugData:
    dc_gain: float
    dc_phase: float
    dc_correction: Tuple[float, float, float, float]


@dataclass
class LOAnalysisDebugData:
    i_scan: Array
    q_scan: Array
    lo: Array
    fit: FitResult
    corrections: CorrectionsDebugData


def _get_and_analyze_lo_data(
    job: Union[RunningQmJob, JobApi], lo_res: int, offset: int, count: int
) -> Tuple[Array, Array, List[LOAnalysisDebugData]]:
    data = _get_reshaped_data(job, lo_res, offset, count, Names.i_scan, Names.q_scan, Names.lo)

    calibration_pulse_amp = 0.25  # TODO(nofek): take it from the right place

    i_scan_full = data[Names.i_scan] * calibration_pulse_amp
    q_scan_full = data[Names.q_scan] * calibration_pulse_amp
    lo_full = data[Names.lo]

    q0_shift = []
    i0_shift = []
    debug_data = []
    for ind in range(i_scan_full.shape[0]):
        i_scan = i_scan_full[ind]
        q_scan = q_scan_full[ind]
        lo = lo_full[ind]

        q = q_scan[0, :]
        i = i_scan[:, 0]
        if np.min(lo) < 0:
            logger.warning("POSSIBLE OVERFLOW!!!")  # TODO: deal with it
        ii, iq = divmod(int(np.argmin(lo)), lo_res)
        ll = min(iq, lo_res - 1 - iq, ii, lo_res - 1 - ii, 7)
        if ll > 3:
            fit = _paraboloid2d_fit(
                q[iq - ll : iq + ll + 1], i[ii - ll : ii + ll + 1], lo[ii - ll : ii + ll + 1, iq - ll : iq + ll + 1]
            )
        else:
            fit = _paraboloid2d_fit(q, i, lo)

        q0_shift.append(fit.x_min)
        i0_shift.append(fit.y_min)

        _I2c, _IQc, _Q2c = fit.pol.take([5, 4, 3])
        _n = np.sqrt(_I2c * _Q2c)
        _I2c, _IQc, _Q2c = _I2c / _n, _IQc / _n, _Q2c / _n

        dc_gain = (_Q2c / _I2c) ** 0.25
        dc_phase = np.arcsin(-_IQc / 2) / 2

        c = np.cos(dc_phase) / np.cos(2 * dc_phase)
        s = np.sin(dc_phase) / np.cos(2 * dc_phase)
        g = dc_gain

        dc_correction = (g * c, g * s, s / g, c / g)

        # Matching the meaning of the phase and gain to that of the calibration
        dc_phase = np.sin(dc_phase) / np.cos(2 * dc_phase)
        dc_gain = (1 + 2 * (dc_gain - 1)) ** 0.5 - 1

        corrections = CorrectionsDebugData(dc_gain=dc_gain, dc_phase=dc_phase, dc_correction=dc_correction)

        debug_data.append(LOAnalysisDebugData(i_scan=i_scan, q_scan=q_scan, lo=lo, fit=fit, corrections=corrections))

    return np.array(i0_shift), np.array(q0_shift), debug_data


@dataclass
class ImageDataAnalysisResult:
    phase: float
    gain: float
    correction: Tuple[float, float, float, float]
    g_scan: Array
    p_scan: Array
    fit: FitResult
    image: Array


def _get_and_analyze_image_data(
    job: Union[RunningQmJob, JobApi], image_res: int, offset: int, count: int
) -> List[ImageDataAnalysisResult]:
    data = _get_reshaped_data(job, image_res, offset, count, Names.g_scan, Names.p_scan, Names.image)

    g_scan_full = data[Names.g_scan]
    p_scan_full = data[Names.p_scan]
    image_full = data[Names.image]

    results = []
    for ind in range(g_scan_full.shape[0]):
        g_scan = g_scan_full[ind]
        p_scan = p_scan_full[ind]
        image = image_full[ind]
        p = p_scan[0, :]
        g = g_scan[:, 0]

        if np.min(image) < 0:
            logger.warning("POSSIBLE OVERFLOW!!!")  # TODO deal with it

        ig, ip = divmod(int(np.argmin(image)), image_res)
        ll = min(ip, image_res - 1 - ip, ig, image_res - 1 - ig, 5)

        sg = g[ig - ll : ig + ll + 1]
        sp = p[ip - ll : ip + ll + 1]

        s_im = image[ig - ll : ig + ll + 1, ip - ll : ip + ll + 1]

        fit = _paraboloid2d_fit(sp, sg, s_im)

        s = fit.x_min
        c = np.polyval([-3.125, 1.5, 1], s**2)
        g_plus = np.polyval([0.5, 1, 1], fit.y_min)
        g_minus = np.polyval([0.5, -1, 1], fit.y_min)

        c00 = float(g_plus * c)
        c01 = float(g_plus * s)
        c10 = float(g_minus * s)
        c11 = float(g_minus * c)

        results.append(
            ImageDataAnalysisResult(
                phase=fit.x_min,
                gain=fit.y_min,
                correction=(c00, c01, c10, c11),
                g_scan=g_scan,
                p_scan=p_scan,
                fit=fit,
                image=image,
            )
        )

    return results
