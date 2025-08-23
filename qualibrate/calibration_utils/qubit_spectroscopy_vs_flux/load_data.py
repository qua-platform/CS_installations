
from pathlib import Path
from datetime import datetime
import xarray as xr
from qualibrate_config.resolvers import get_qualibrate_config, get_qualibrate_config_path

def get_storage_root() -> Path:
    q_config_path = get_qualibrate_config_path()
    qs = get_qualibrate_config(q_config_path)
    return Path(qs.storage.location)

def _is_date_folder(p: Path, date_fmt: str = "%Y-%m-%d") -> bool:
    try:
        datetime.strptime(p.name, date_fmt)
        return True
    except ValueError:
        return False

def get_latest_date_folder(base_path: str | Path = None, date_fmt: str = "%Y-%m-%d") -> Path:
    """
    If base_path is a folder *named like a date*, return it.
    Otherwise, treat base_path (or storage root if None) as the parent that contains date-named subfolders,
    and return the newest one.
    """
    base = Path(base_path).resolve() if base_path is not None else get_storage_root()

    if not base.exists():
        raise FileNotFoundError(f"{base} not found (cwd={Path.cwd()})")

    # If user already passed a date folder, just return it
    if base.is_dir() and _is_date_folder(base, date_fmt=date_fmt):
        return base

    # Otherwise, search its immediate subfolders for date-named dirs
    candidates = []
    for p in base.iterdir():
        if p.is_dir() and _is_date_folder(p, date_fmt=date_fmt):
            dt = datetime.strptime(p.name, date_fmt)
            candidates.append((dt, p))

    if not candidates:
        raise RuntimeError(f"No dated folders found in {base}")

    candidates.sort(key=lambda x: x[0])
    return candidates[-1][1]

def get_latest_res_spec_folder(base_path: str | Path = None, date_fmt: str = "%Y-%m-%d") -> Path:
    """
    Accepts:
      - storage root,
      - project folder,
      - or a specific date folder (YYYY-MM-DD).
    Finds the newest subfolder whose name contains 'resonator_spectroscopy_vs_flux'
    inside the resolved date folder.
    """
    latest_date_folder = get_latest_date_folder(base_path, date_fmt=date_fmt)

    matches = [p for p in latest_date_folder.iterdir()
               if p.is_dir() and "resonator_spectroscopy_vs_flux" in p.name.lower()]
    if not matches:
        raise RuntimeError(f"No resonator_spectroscopy_vs_flux folder found in {latest_date_folder}")

    matches.sort(key=lambda p: p.stat().st_mtime)
    return matches[-1]

def load_ds_fit(path: str | Path):
    """
    Load ds_fit.h5 saved by Qualibrate into (xarray.Dataset, dict of fit params).
    Your files are NetCDF (scipy engine), despite .h5 extension.
    """
    ds = xr.load_dataset(Path(path), engine="scipy")
    labels = ds["fit_vals"].values.tolist()
    fits = {
        qb: dict(zip(labels, ds["fit_results"].sel(qubit=qb).values.tolist()))
        for qb in ds["qubit"].values.tolist()
    }
    return ds, fits
