# ======================================================================
#  rb1q_dashboard.py   (FULL / REVISED)
# ======================================================================
"""
Dash module for **1Q Randomized‑Benchmarking** experiments
==========================================================
* 1‑D    : circuit‑depth  →  averaged qubit‑state  (± fit)
* Layout : >=10 qubits support, 2 columns × N rows + pagination (8 qubits/page)
--------------------------------------------------------------------
"""
from __future__ import annotations

import os, json
from pathlib import Path
from typing import Any

import dash
from dash import dcc, html, Input, Output, State, MATCH
import dash_bootstrap_components as dbc
import numpy as np
import xarray as xr
import plotly.graph_objs as go
import plotly.subplots as subplots


# ────────────────────────────────────────────────────────────────────
# 0. Common utilities
# ────────────────────────────────────────────────────────────────────
PER_PAGE = 16           # qubits per page
N_COLS   = 2            # subplot columns
MAX_VALID_FIDELITY = 99.999999  # This value is considered unrealistic


def open_xr_dataset(path: str, engines=("h5netcdf", "netcdf4", None)) -> xr.Dataset:
    """Open xarray Dataset with automatic engine switching attempts."""
    last_exc: Exception | None = None
    for eng in engines:
        try:
            return xr.open_dataset(path, engine=eng)
        except Exception as e:  # pragma: no cover
            last_exc = e
    raise last_exc if last_exc else RuntimeError(f"Cannot open dataset: {path}")


def decay_exp(x: np.ndarray, a: float, offset: float, decay: float) -> np.ndarray:
    """RB decay model – offset + a·exp(decay·x)"""
    return offset + a * np.exp(decay * x)


# ────────────────────────────────────────────────────────────────────
# 1. Data loader
# ────────────────────────────────────────────────────────────────────
def load_rb_data(folder: str | Path) -> dict[str, Any] | None:
    """
    Load 4 RB result files (ds_raw.h5, ds_fit.h5, data.json, node.json)
    from folder (or absolute path) and return in dict format ready for
    direct use in Dash frontend.

    Return fields
    ----------
    qubits          ndarray[str]   (q)
    n               int            number of qubits
    depths          ndarray[float] (d)
    y_data          ndarray        (q, d)  • averaged qubit state
    success         ndarray[bool]  (q)     • fit success status
    rb_fidelity     ndarray        (q)     • 100 × (1 – error_per_gate)
    fit_a/offset/decay             (q)     • fit parameters
    ds_raw, ds_fit                original datasets (for use if needed)
    data_json, node_json          metadata
    """
    folder = Path(folder).expanduser().resolve()
    paths = {
        "ds_raw":  folder / "ds_raw.h5",
        "ds_fit":  folder / "ds_fit.h5",
        "data_js": folder / "data.json",
        "node_js": folder / "node.json",
    }
    if not all(p.exists() for p in paths.values()):
        print(f"[load_rb_data] Required files not found in {folder}")
        return None

    # ── File loading ─────────────────────────────────────────────────
    ds_raw  = open_xr_dataset(str(paths["ds_raw"]))
    ds_fit  = open_xr_dataset(str(paths["ds_fit"]))
    data_js = json.loads(paths["data_js"].read_text(encoding="utf-8"))
    node_js = json.loads(paths["node_js"].read_text(encoding="utf-8"))

    qubits = ds_fit.get("qubit", ds_raw["qubit"]).values.astype(str)
    n_q    = len(qubits)

    # ── depth axis ────────────────────────────────────────────────
    depths = (
        ds_fit.coords["depths"]
        if "depths" in ds_fit.coords
        else ds_fit.coords.get("circuit_depth", None)
    )
    if depths is None:
        raise KeyError("'depths' coordinate not found in ds_fit.")
    depths = depths.values.astype(float)

    # ── Average state data (y-axis) ────────────────────────────────────
    if "averaged_data" in ds_fit:
        y_data = ds_fit["averaged_data"].values                      # (q, d)
    elif "averaged_data" in ds_raw:
        y_data = ds_raw["averaged_data"].values                      # (q, d)
    elif "state" in ds_fit:                                          # (q, seq, d)
        y_data = ds_fit["state"].mean(dim="nb_of_sequences").values
    else:
        raise KeyError("averaged_data/state variable not found.")

    # ── Fitting parameters ────────────────────────────────────────────
    def _param_from(name: str) -> np.ndarray:
        if "fit_data" in ds_fit:
            return ds_fit["fit_data"].sel(fit_vals=name).values
        return ds_fit.get(name, np.full(n_q, np.nan)).values  # type: ignore

    fit_a      = _param_from("a")
    fit_offset = _param_from("offset")
    fit_decay  = _param_from("decay")

    # ── Success status ───────────────────────────────────────────────
    if "success" in ds_fit:
        success = ds_fit["success"].values.astype(bool)
    else:
        # If not available, use error_per_gate validity as substitute
        success = ~np.isnan(_param_from("decay"))

    # ── RB fidelity (using error_per_gate) ─────────────────────────────
    rb_fid = np.full(n_q, np.nan)
    for i, q in enumerate(qubits):
        res = data_js.get("fit_results", {}).get(str(q), {})
        if "error_per_gate" in res and res["error_per_gate"] is not None:
            rb_fid[i] = 100.0 * (1.0 - float(res["error_per_gate"]))

    return dict(
        qubits=qubits, n=n_q,
        depths=depths, y_data=y_data,
        success=success, rb_fidelity=rb_fid,
        fit_a=fit_a, fit_offset=fit_offset, fit_decay=fit_decay,
        ds_raw=ds_raw, ds_fit=ds_fit,
        data_json=data_js, node_json=node_js,
    )


# ────────────────────────────────────────────────────────────────────
# 1‑B. Pagination helper
# ────────────────────────────────────────────────────────────────────
def slice_page(data: dict[str, Any], page: int) -> dict[str, Any]:
    """Slice only qubit dimension (q), return sub-dict (maintaining depth·metadata)."""
    if not data:
        return data
    start = (page - 1) * PER_PAGE
    stop  = min(page * PER_PAGE, data["n"])
    s_qub = slice(start, stop)

    sliced = data.copy()
    for key in ("qubits", "y_data", "success",
                "rb_fidelity", "fit_a", "fit_offset", "fit_decay"):
        sliced[key] = data[key][s_qub]
    sliced["n"] = len(sliced["qubits"])
    return sliced


# ────────────────────────────────────────────────────────────────────
# 2. Plot generation
# ────────────────────────────────────────────────────────────────────
def create_rb_plot(d: dict[str, Any]) -> go.Figure:
    """Return Plotly subplots Figure (Data + Fit)."""
    if not d:
        return go.Figure()

    qbs, n_q      = d["qubits"], d["n"]
    depths        = d["depths"]
    y_data        = d["y_data"]
    success       = d["success"]
    fit_a, fit_o, fit_d = d["fit_a"], d["fit_offset"], d["fit_decay"]
    rb_fidelity   = d["rb_fidelity"]

    n_rows = int(np.ceil(n_q / N_COLS))
    fig = subplots.make_subplots(
        rows=n_rows, cols=N_COLS,
        subplot_titles=[str(q) for q in qbs],
        vertical_spacing=0.03, horizontal_spacing=0.07,
    )

    for i, q in enumerate(qbs):
        r, c = divmod(i, N_COLS)
        row, col = r + 1, c + 1

        # ── Raw data (markers) ────────────────────────────────────
        fig.add_trace(
            go.Scatter(
                x=depths,
                y=y_data[i],
                mode="markers",
                marker=dict(size=6, color="royalblue"),
                name="Data" if i == 0 else None,
                showlegend=(i == 0),
            ),
            row=row, col=col,
        )

        # ── Fit curve (only for valid results) ───────────────────
        fid_val = rb_fidelity[i]
        fit_valid = (bool(success[i]) and 
                    not np.isnan(fit_d[i]) and 
                    not (fid_val >= MAX_VALID_FIDELITY))  # 비현실적인 값 제외

        if fit_valid:
            y_fit = decay_exp(depths, fit_a[i], fit_o[i], fit_d[i])
            fig.add_trace(
                go.Scatter(
                    x=depths, y=y_fit,
                    mode="lines",
                    line=dict(color="firebrick", dash="dash"),
                    name="Fit" if i == 0 else None,
                    showlegend=(i == 0),
                ),
                row=row, col=col,
            )

        # Axis labels (only at bottom/left)
        if row == n_rows:
            fig.update_xaxes(title_text="Circuit depth", row=row, col=col)
        if col == 1:
            fig.update_yaxes(title_text="Qubit state", row=row, col=col)

    fig.update_layout(
        title="Single‑qubit Randomized‑Benchmarking",
        height=max(250, 380*n_rows),
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
        margin=dict(t=60, l=50, r=30, b=50),
    )
    return fig


# ────────────────────────────────────────────────────────────────────
# 3. Summary Table
# ────────────────────────────────────────────────────────────────────
def create_summary_table(d: dict[str, Any]) -> dbc.Table:
    rows: list[html.Tr] = []
    for i, q in enumerate(d["qubits"]):
        
        ok = bool(d["success"][i])
        
        fid_val = d["rb_fidelity"][i]
        if np.isnan(fid_val) | (fid_val >= MAX_VALID_FIDELITY):
            fid_txt = "-"
            row_class = "table-warning" 
            ok = False
        else:
            fid_txt = f"{fid_val:.3f} %"
            row_class = "table-success" if ok else "table-warning"
        
        rows.append(
            html.Tr(
                [
                    html.Td(q),
                    html.Td(fid_txt),
                    html.Td("✓" if ok else "✗"),
                ],
                className=row_class,
            )
        )

    thead = html.Thead(
        html.Tr([html.Th("Qubit"),
                 html.Th("1Q RB fidelity"),
                 html.Th("Fit")])
    )
    return dbc.Table([thead, html.Tbody(rows)],
                     bordered=True, striped=True, size="sm", responsive=True)


# ────────────────────────────────────────────────────────────────────
# 4. Layout generation
# ────────────────────────────────────────────────────────────────────
def create_rb_layout(folder: str | Path) -> html.Div:
    """
    Called externally as `app.layout = create_rb_layout(<experiment_folder>)`.
    """
    uid = str(folder).replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_rb_data(folder)
    if not data:
        return html.Div([dbc.Alert("Data loading failed", color="danger"),
                         html.Pre(str(folder))])

    n_pages = int(np.ceil(data["n"] / PER_PAGE))
    init_fig = create_rb_plot(slice_page(data, 1))

    # ── Pagination component ─────────────────────────────────────────
    page_selector = dbc.Pagination(
        id={"type": "rb-page", "index": uid},
        active_page=1,
        max_value=n_pages,
        first_last=True,
        fully_expanded=False,
        size="lg",
        className="my-2",
        style=None if n_pages > 1 else {"display": "none"},
    )

    # ── Layout ----------------------------------------------------
    return html.Div(
        [
            # Data caching
            dcc.Store(id={"type": "rb-data", "index": uid},
                      data={"folder": str(folder)}),

            # Title
            dbc.Row(
                dbc.Col(html.H3(f"1Q Randomized Benchmark – {Path(folder).name}")),
                className="mb-3",
            ),

            # Pagination
            dbc.Row(dbc.Col(page_selector), className="mb-2"),

            # Graph + Summary
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Loading(
                            id={"type": "rb-load", "index": uid},
                            type="default",
                            children=dcc.Graph(
                                id={"type": "rb-plot", "index": uid},
                                figure=init_fig,
                                config={"displayModeBar": True},
                            ),
                        ),
                        md=8,
                    ),
                    dbc.Col(
                        [
                            html.H5("Summary"),
                            create_summary_table(data),
                            html.Hr(),
                            html.Small(f"Folder: {folder}"),
                        ],
                        md=4,
                    ),
                ]
            ),
        ],
        className="p-3",
    )


# ────────────────────────────────────────────────────────────────────
# 5. Callback registration
# ────────────────────────────────────────────────────────────────────
def register_rb_callbacks(app: dash.Dash):
    """
    Register callbacks to Dash app instance.
    Must call `register_rb_callbacks(app)` after app creation.
    """

    @app.callback(
        Output({"type": "rb-plot", "index": MATCH}, "figure"),
        Input({"type": "rb-page", "index": MATCH}, "active_page"),
        State({"type": "rb-data", "index": MATCH}, "data"),
        prevent_initial_call=True,
    )
    def _update_rb_plot(active_page: int, store: dict[str, str]) -> go.Figure:
        folder = store.get("folder")
        if not folder:
            return go.Figure()
        data = load_rb_data(folder)
        return create_rb_plot(slice_page(data, active_page or 1))


# ────────────────────────────────────────────────────────────────────
# 6. Stand‑alone execution (for testing)
# ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    SAMPLE_PATH = "./"           # ← Change to folder with RB result files
    app = dash.Dash(__name__,
                    external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = create_rb_layout(SAMPLE_PATH)
    register_rb_callbacks(app)

    app.run_server(debug=True, port=8073)
