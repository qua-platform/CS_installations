# QUAlibrate Dashboard

A **Dash + Plotly** web application for **QUAlibration Experiment Data**.
It lets you explore relevant experiments from one browser tab.

---

## 1 · What this repository is about

| Topic              | Details                                                                                                                                                                                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**        | Provide a uniform, low‑friction UI for *analysts, experimentalists and operators* to inspect the raw data, fitted curves, and summary tables that come out of daily calibration runs on a superconducting‑qubit platform.                                                    |
| **Input data**     | Each experiment folder contains four required files produced by the data‑acquisition back‑end: `ds_raw.h5`, `ds_fit.h5`, `data.json`, `node.json`                                                                    |
| **Core idea**      | **One experiment = One Plotly-Dash .py file** living under `experiments/<name>_dashboard.py`.  The top‑level `main_dashboard.py` automatically discovers experiment folders, loads the correct module, and injects its *layout* and *callbacks* into the main Dash `app`. |
---

## 2 · Build the Python environment

> **TL;DR – conda users**

```bash
conda create -n qualib_dash python=3.12
conda activate qualib_dash
pip install -r requirements.txt
```

### 2.1 Prerequisites

| Tool                    | Version    | Why                         |
| ----------------------- | ---------- | --------------------------- |
| Python                  | 3.9 – 3.12 | Tested on 3.12              |

---

## 3 · Use the dashboard from scratch

1. **Clone** the repository

   ```bash
   git clone https://github.com/your‑org/qualibrate‑dashboard.git
   cd qualibrate‑dashboard
   ```

2. **Prepare** the environment (see § 2).

3. **Point** the app at your experiment archive

   - **Default base folder**  
     The app looks in `[Project_Folder_Path]`. The following is the path in this current repo:

     ```python
     EXPERIMENT_BASE_PATH = os.environ.get("EXPERIMENT_BASE_PATH", os.path.join(BASE, "data/QPU_Project"))
     ```

   - **To change it**, simply edit "data/QPU_Project" to your desired data folder path.

   - **Data folder structure**  
     Your calibration data must live under `EXPERIMENT_BASE_PATH` with this layout:

     ```text
     EXPERIMENT_BASE_PATH/
     ├─ 2025-06-23/                    # date folder: YYYY-MM-DD
     │   ├─ #1094_01b_time_of_flight/  # experiment folder: #<runID>_<type>_<timestamp>
     │   │   ├─ ds_raw.h5
     │   │   ├─ ds_fit.h5
     │   │   ├─ data.json
     │   │   └─ node.json
     │   ├─ #1095_qubit_spectroscopy…/
     │   └─ … (other experiments)
     ├─ 2025-06-24/
     │   └─ #1100_resonator_spectroscopy_…/
     └─ 2025-06-25 ...
     ```

     - **Date folders** (`YYYY-MM-DD`) group all runs from that day.  
     - **Experiment folders** must contain exactly four files (as saved by QUAlibrate):
       1. `ds_raw.h5`  
       2. `ds_fit.h5`  
       3. `data.json`  
       4. `node.json`  
     - Folder names **must** start with `#<numeric_id>` and end with a 6-digit timestamp.  
     - Dash will only display folders matching this pattern **and** containing all four files.


4. **Launch** the server

   ```bash
   python main_dashboard.py
   ```

   By default the server is started on `http://127.0.0.1:7700/` with live‑reload (`debug=True`).
   Open the URL and:

   1. Choose an **experiment type** from the first dropdown (Time‑of‑Flight, T1, RB, …).
   2. Pick a **date/time‑stamped run** from the second dropdown.
   3. Enjoy the reactive plots, summary tables, pagination and dark theme.

5. **Troubleshooting**

   *“Files not found”* alerts mean the required quartet (`ds_raw.h5`, `ds_fit.h5`, 2× \*.json) is missing.
   *90 % of display problems* are wrong `plotly.io.templates.default` – run `python -m pip install --upgrade plotly` first.

---

## 4 · Adding another experiment module

> The framework is deliberately minimal – you only implement three things and the rest is auto‑wired.

```text
experiments/
├─ myexperiment_dashboard.py      ◀─ sdd your new experiment file
```

### 4.1 Skeleton to copy‑paste

```python
# experiments/myexperiment_dashboard.py
import dash
from dash import dcc, html, Input, Output, State, MATCH
...

# 1. ------------- Data loader ---------------------------------
def load_myexp_data(folder: str | Path) -> dict | None:
    """Read ds_raw.h5 etc. and return a tidy dict used by plotting
       • MUST return at least 'qubits' and 'n'."""
    ...
    return {...}

# 2‑A. ------------- Plot creators ------------------------------
def create_myexp_plot(data: dict, *args, **kwargs) -> go.Figure:
    ...

# 2‑B. (optional) summary table, helpers, etc.

# 3. ------------- Layout factory -------------------------------
def create_myexp_layout(folder: str | Path):
    ...

    return html.Div([
        ...
        dcc.Graph(id={"type": "myexp-plot", "index": uid},
                  figure=init_fig),
        ...
    ])

# 4. ------------- Callback registration -----------------------
def register_myexp_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": "myexp-plot", "index": MATCH}, "figure"),
        Input (...),
        State(...),
    )
    def _update_plot(...):
        data = load_myexp_data(store["folder"])
        return create_myexp_plot(data, ...)
```

### 4.2 Hook it into the main app

1. **Import** and **register** in `main_dashboard.py`

   ```python
   from experiments.myexperiment_dashboard \
       import create_myexp_layout, register_myexp_callbacks
   ```

2. **Extend** the `experiment_modules` dict

   ```python
   "myexp": dict(
       layout_func   = create_myexp_layout,
       register_func = register_myexp_callbacks,
       title         = "My Experiment",
       patterns      = ["myexp", "my_exp", "whatever_in_folder_name"], → keywords to search for folders
   ),
   ```

3. **Add** the callback registration line near the bottom:

   ```python
   register_myexp_callbacks(app)
   ```

> Auto-reload: the dashboard will now auto‑detect any folder whose name contains one of your `patterns` keywords.

---

## 5 · Repository overview

```
├─ main_dashboard.py         ← entry point / routing / folder polling
├─ assets/                   ← CSS & image assets (dark theme, logo …)
├─ experiments/              ← one module per calibration
│   ├─ t1_dashboard.py
│   ├─ ramsey_dashboard.py
│   ├─ ...                   (11 modules today)
│   └─ myexperiment_dashboard.py   ← your new one
├─ theme.py                  ← Plotly template registration
├─ requirements.txt
└─ README.md                 ← you are here
```

---

## 6 · Additional Features

* **Hot‑reloading** – Dash already reloads Python & CSS on file save when `debug=True`.
* **Deployment** – Any WSGI container (Gunicorn/uvicorn) works.  Remember to set `debug=False` and adjust `host='0.0.0.0'`.
* **Large data files** – If `ds_raw.h5` exceeds 200 MB use *indexed* `zarr` or supply a down‑sampled version for the dashboard.

---

### Happy calibrating & plotting! 🎉