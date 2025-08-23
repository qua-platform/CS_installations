import xarray as xr
from pathlib import Path
from datetime import datetime


def get_latest_date_folder(base_path: str | Path, project_name="QPU_project") -> Path:
    base_path = Path(base_path) / project_name
    if not base_path.exists():
        raise FileNotFoundError(f"{base_path} not found")

    candidates = []
    for p in base_path.iterdir():
        if p.is_dir():
            try:
                date_val = datetime.strptime(p.name, "%Y-%m-%d")
                candidates.append((date_val, p))
            except ValueError:
                pass
    if not candidates:
        raise RuntimeError(f"No dated folders found in {base_path}")
    candidates.sort(key=lambda x: x[0])
    return candidates[-1][1]


def get_latest_res_spec_folder(base_path: str | Path, project_name="QPU_project") -> Path:
    """
    Go into the latest date folder inside project_name,
    then find the latest subfolder containing 'resonator_spectroscopy_vs_flux'.
    """
    latest_date_folder = get_latest_date_folder(base_path, project_name)

    # all matching subfolders
    matches = [p for p in latest_date_folder.iterdir()
               if p.is_dir() and "resonator_spectroscopy_vs_flux" in p.name.lower()]
    if not matches:
        raise RuntimeError(f"No resonator_spectroscopy_vs_flux folder found in {latest_date_folder}")

    # sort by mtime in case there are multiple
    matches.sort(key=lambda p: p.stat().st_mtime)
    return matches[-1]


def load_ds_fit(path: str):
    """
    Load ds_fit.h5 saved by Qualibrate into (xarray.Dataset, dict of fit params).
    """
    ds = xr.load_dataset(path, engine="scipy")
    labels = ds["fit_vals"].values.tolist()
    fits = {
        qb: dict(zip(labels, ds["fit_results"].sel(qubit=qb).values.tolist()))
        for qb in ds["qubit"].values.tolist()
    }
    return ds, fits