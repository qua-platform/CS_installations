import dash
from dash import dcc, html, Input, Output, State, clientside_callback, ClientsideFunction
import dash_bootstrap_components as dbc
from datetime import datetime
import os, re
from pathlib import Path
import theme
from dash_bootstrap_templates import load_figure_template
import plotly.io as pio
# ────────────────────────────────────────────────────────────────────
# Import Dash modules for each experiment
# ────────────────────────────────────────────────────────────────────
from experiments.tof_dashboard        import create_tof_layout,   register_tof_callbacks
from experiments.resonator_dashboard  import create_res_layout,   register_res_callbacks
from experiments.qspec_dashboard      import create_qspec_layout, register_qspec_callbacks
from experiments.power_rabi_dashboard import create_prabi_layout, register_prabi_callbacks
from experiments.t1_dashboard         import create_t1_layout,    register_t1_callbacks
from experiments.echo_dashboard       import create_t2_echo_layout,  register_t2_echo_callbacks
from experiments.ramsey_dashboard     import create_t2_ramsey_layout, register_t2_ramsey_callbacks
from experiments.iq_dashboard         import create_iq_blob_layout,    register_iq_blob_callbacks
from experiments.readout_power_opt_dashboard import create_rpo_layout, register_rpo_callbacks
from experiments.drag_dashboard       import create_drag_layout,   register_drag_callbacks
from experiments.rb1q_dashboard       import create_rb_layout,     register_rb_callbacks     
# ────────────────────────────────────────────────────────────────────
# App instance & global settings
# ────────────────────────────────────────────────────────────────────
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                assets_folder="assets",
                suppress_callback_exceptions=True)
server = app.server

# Load both figure templates
load_figure_template(["bootstrap", "slate"])
import os
BASE = os.path.abspath(os.path.dirname(__file__))
EXPERIMENT_BASE_PATH = os.environ.get("EXPERIMENT_BASE_PATH", os.path.join(BASE, "data/QPU_Project"))
EXPERIMENT_BASE_PATH = './'

# Default experiment type metadata ------------------------------------------------
DEFAULT_EXPERIMENT_MODULES = {
    "tof": dict(
        layout_func=create_tof_layout,
        register_func=register_tof_callbacks,
        title="Time of Flight",
        patterns=["tof", "time_of_flight"],
        exclude_patterns=[],  # No exclusions for TOF
        is_custom=False,
    ),
    "res": dict(
        layout_func=create_res_layout,
        register_func=register_res_callbacks,
        title="Resonator Spectroscopy",
        patterns=["res_spec", "resonator", "resonator_spectroscopy"],
        exclude_patterns=["power", "power_amp", "vs_power", "power_sweep"],  # Exclude power-related resonator experiments
        is_custom=False,
    ),
    "qspec": dict(
        layout_func=create_qspec_layout,
        register_func=register_qspec_callbacks,
        title="Qubit Spectroscopy",
        patterns=["qspec", "qubit_spec", "qubit_spectroscopy"],
        exclude_patterns=["power", "vs_power", "power_sweep"],  # Exclude power-related qubit spectroscopy
        is_custom=False,
    ),
    "prabi": dict(
        layout_func=create_prabi_layout,
        register_func=register_prabi_callbacks,
        title="Rabi Error Amp",
        patterns=["prabi", "error"],
        exclude_patterns=[],  # No exclusions for power rabi
        is_custom=False,
    ),
    "t1": dict(
        layout_func=create_t1_layout,
        register_func=register_t1_callbacks,
        title="T1 Relaxation",
        patterns=["t1", "t1_relax", "relaxation"],
        exclude_patterns=["vs_power", "power_sweep", "power_dep"],  # Exclude power-dependent T1
        is_custom=False,
    ),
    "echo": dict(
        layout_func=create_t2_echo_layout,
        register_func=register_t2_echo_callbacks,
        title="T2 Echo",
        patterns=["echo", "t2echo", "t2_echo", "t2e"],
        exclude_patterns=["vs_power", "power_sweep", "power_dep"],  # Exclude power-dependent echo
        is_custom=False,
    ),
    "ramsey": dict(
        layout_func=create_t2_ramsey_layout,
        register_func=register_t2_ramsey_callbacks,
        title="Ramsey (T2*)",
        patterns=["ramsey", "t2star", "t2*", "ramsey_exp"],
        exclude_patterns=["vs_power", "power_sweep", "power_dep"],  # Exclude power-dependent ramsey
        is_custom=False,
    ),
    "iq": dict(
        layout_func=create_iq_blob_layout,
        register_func=register_iq_blob_callbacks,
        title="IQ Discrimination",
        patterns=["iq", "iq_blobs", "iq_readout"],
        exclude_patterns=["vs_power", "power_sweep"],  # Exclude power-dependent IQ
        is_custom=False,
    ),
    "rpo": dict(
        layout_func=create_rpo_layout,
        register_func=register_rpo_callbacks,
        title="Readout Power Opt.",
        patterns=["readout_power", "power_opt", "readout_power_optimization",
                  "rpo", "readout‑power"],
        exclude_patterns=[],  # This IS a power experiment, so no power exclusions
        is_custom=False,
    ),
    "drag": dict(
        layout_func=create_drag_layout,
        register_func=register_drag_callbacks,
        title="DRAG Calibration",
        patterns=["drag", "drag_cal", "dragcal", "drag_calibration"],
        exclude_patterns=["vs_power", "power_sweep", "power_dep"],  # Exclude power-dependent DRAG
        is_custom=False,
    ),
    "rb1q": dict(                             
        layout_func=create_rb_layout,
        register_func=register_rb_callbacks,
        title="1Q Randomized Benchmark",
        patterns=["rb1q", "1q_rb", "Randomized", "Randomized_benchmarking", "benchmarking"],
        exclude_patterns=["vs_power", "power_sweep", "power_dep"],  # Exclude power-dependent RB
        is_custom=False,
    ),
}
# Global variable that will be updated by user interactions
experiment_modules = DEFAULT_EXPERIMENT_MODULES.copy()
def get_experiment_modules():
    """Get current experiment modules (including custom ones)"""
    return experiment_modules

def update_experiment_modules_from_custom_types(custom_types):
    """Update global experiment modules with custom types (without function references)"""
    global experiment_modules
    # Start with default modules
    updated_modules = DEFAULT_EXPERIMENT_MODULES.copy()
    
    # Add custom types with generic functions
    for key, value in custom_types.items():
        # Create a complete module entry with the generic functions
        module_entry = {
            "title": value.get("title", ""),
            "patterns": value.get("patterns", []),
            "exclude_patterns": value.get("exclude_patterns", []),
            "is_custom": True,
            "layout_func": create_generic_layout,  # Assign function directly, not stored
            "register_func": register_generic_callbacks  # Assign function directly, not stored
        }
        updated_modules[key] = module_entry
    
    experiment_modules = updated_modules
    return updated_modules

def create_generic_layout(path):
    """Generic layout for custom experiment types that don't have specific layouts"""
    return html.Div([
        dbc.Alert([
            html.H5("Custom Experiment Category", className="mb-2"),
            html.P(f"Experiment path: {path}"),
            html.P("This is a custom experiment category. No specific visualization is available yet."),
            html.P("The experiment files are detected and categorized based on your custom filters.")
        ], color="info")
    ])
def register_generic_callbacks(app):
    """Generic callback registration for custom experiment types"""
    pass  # No specific callbacks needed for generic custom experiments


# ────────────────────────────────────────────────────────────────────
# 1. Enhanced Scan experiment folders with filtering (using experiment_modules)
# ────────────────────────────────────────────────────────────────────
def find_experiments(base_path: str):
    """
    Date folders: YYYY_MM_DD or YYYY-MM-DD
    Experiment folders: '#number_…<keyword>…_<HHMMSS>'
    Enhanced with exclude_patterns filtering to filter out directories with specific keywords
    """
    exps: dict[str, list] = {}
    base_path = os.path.normpath(base_path)
    if not os.path.exists(base_path):
        return exps
    date_re = re.compile(r"^\d{4}[-_]\d{2}[-_]\d{2}$")
    date_dirs = [
        d for d in os.listdir(base_path)
        if date_re.match(d) and os.path.isdir(Path(base_path, d))
    ]
    
    # Get current experiment modules (which may include user modifications)
    current_modules = get_experiment_modules()
    
    # MODIFICATION: Prioritize custom types over default types
    custom_types = [(k, v) for k, v in current_modules.items() if v.get("is_custom", False)]
    default_types = [(k, v) for k, v in current_modules.items() if not v.get("is_custom", False)]
    ordered_modules = custom_types + default_types
    
    for dname in date_dirs:
        y, m, d = map(int, re.split(r"[-_]", dname))
        day_dir = Path(base_path, dname)
        for exp_dir in day_dir.iterdir():
            if not exp_dir.is_dir():
                continue
            fname = exp_dir.name.lower()
            fname = str(Path(dname) / exp_dir.name).lower()

            # Check if required data files exist
            required_ok = all(
                (exp_dir / f).exists()
                for f in ("ds_raw.h5", "ds_fit.h5")
            ) and len(list(exp_dir.glob("*.json"))) >= 2
            if not required_ok:
                continue
            
            # Determine experiment type with enhanced filtering
            matched_type = None
            
            # Check ordered modules (custom first, then default)
            for typ, info in ordered_modules:
                # First check if any pattern matches (case-insensitive)
                patterns = [p.lower() for p in info["patterns"]]
                pattern_match = any(p in fname for p in patterns)
                
                if not pattern_match:
                    continue
                
                # Then check if any exclude pattern matches (filter out if found)
                exclude_patterns = [ep.lower() for ep in info.get("exclude_patterns", [])]
                exclude_match = any(ep in fname for ep in exclude_patterns)
                
                if exclude_match:
                    # Log filtered out experiments for debugging
                    # print(f"[FILTER] Excluding {fname} from {typ} due to exclude patterns: {exclude_patterns}")
                    continue
                
                # If pattern matches and no exclude pattern matches, this is our type
                matched_type = typ
                # print(f"[MATCH] {fname} matched to type: {typ} (custom={info.get('is_custom', False)})")
                break  # Stop after first match
            
            if matched_type is None:
                # print(f"[NO MATCH] {fname} did not match any experiment type")
                continue
            
            # Timestamp extraction
            m_t = re.search(r"(\d{6})$", fname)
            hh, mm, ss = (
                int(m_t.group(1)[:2]),
                int(m_t.group(1)[2:4]),
                int(m_t.group(1)[4:]),
            ) if m_t else (0, 0, 0)
            ts = datetime(y, m, d, hh, mm, ss).timestamp()
            
            # Add to experiments list
            exps.setdefault(matched_type, []).append(
                dict(
                    path=str(exp_dir),
                    name=exp_dir.name,
                    date_folder=dname,
                    timestamp=ts,
                    source_folder=base_path,
                )
            )
    
    # Sort each experiment type by timestamp (newest first)
    for typ in exps:
        exps[typ].sort(key=lambda e: e["timestamp"], reverse=True)
    
    return exps


def find_experiments_multiple_paths(paths_list):
    """
    Find experiments from multiple base paths and merge results
    """
    all_exps: dict[str, list] = {}
    
    for base_path in paths_list:
        if base_path and os.path.exists(base_path):
            path_exps = find_experiments(base_path)
            for typ, exp_list in path_exps.items():
                if typ not in all_exps:
                    all_exps[typ] = []
                all_exps[typ].extend(exp_list)
    
    # Sort each experiment type list by timestamp
    for typ in all_exps:
        all_exps[typ].sort(key=lambda e: e["timestamp"], reverse=True)
    
    return all_exps




def get_directory_tree(path, max_depth=3, current_depth=0):
    if current_depth >= max_depth or not os.path.exists(path):
        return []
    
    items = []
    try:
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                items.append(f"{'  ' * current_depth}📁 {item}/")
                if current_depth < max_depth - 1:
                    items.extend(get_directory_tree(item_path, max_depth, current_depth + 1))
            else:
                items.append(f"{'  ' * current_depth}📄 {item}")
    except PermissionError:
        items.append(f"{'  ' * current_depth}❌ Permission denied")
    except Exception as e:
        items.append(f"{'  ' * current_depth}❌ Error: {str(e)}")
    
    return items
# ────────────────────────────────────────────────────────────────────
# 2. Layout
# ────────────────────────────────────────────────────────────────────
app.layout = html.Div([
    # Add stores for filter management
    dcc.Store(id="theme-store", storage_type="local", data="dark"),
    dcc.Store(id="current-experiments", data={}),
    dcc.Store(id="additional-folders", storage_type="local", data=[]),
    dcc.Store(id="folder-remove-trigger", data=0),  # Trigger for folder removal
    dcc.Store(id="disabled-folders", storage_type="local", data=[]),
    dcc.Store(id="custom-experiment-types", storage_type="local", data={}),  # Store for custom experiment types
    dcc.Store(id="filter-update-trigger", data=0),  # Trigger for filter updates
    dcc.Interval(id="folder-check-interval", interval=5000, n_intervals=0),
    
    # Include both dark and light theme CSS
    html.Link(rel="stylesheet", href="/assets/dark_theme.css"),
    html.Link(rel="stylesheet", href="/assets/light_theme.css"),
    
    # Theme toggle button
    html.Button(
        id="theme-toggle",
        className="theme-toggle-btn",
        children=html.Span("☀️", id="theme-icon"),
        n_clicks=0
    ),
    dbc.Container(
        [
            # ── Black top-bar with logo  ───────────────────────
            html.Div(
                className="top-bar",
                style={
                    "position": "relative",
                    "height": "80px",
                    "backgroundColor": "#000000",
                    "marginLeft": "-12px",
                    "marginRight": "-12px",
                    "marginTop": "-12px",
                    "marginBottom": "20px",
                },
                children=[
                    # ── Logo always stuck to the left, vertically centred ──
                    html.Img(
                        src=app.get_asset_url("qm_logo.png"),
                        style={
                            "position": "absolute",
                            "left": "20px",
                            "top": "50%",
                            "transform": "translateY(-50%)",
                            "height": "60px",
                        },
                    ),
                    # ── Title always centred in the bar ──
                    html.H1(
                        "QUAlibrate Dashboard",
                        style={
                            "position": "absolute",
                            "top": "50%",
                            "left": "50%",
                            "transform": "translate(-50%, -50%)",
                            "margin": "0",
                            "color": "#FFFFFF",
                            "fontSize": "32px",
                        },
                        className="text-center",
                    ),
                ],
            ),
            dbc.Row(dbc.Col(html.Div(id="alert-container")), className="mb-3"),
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Button(
                                "🔍 Folder Information",
                                id="debug-toggle-button",
                                color="warning",
                                outline=True,
                                size="sm"
                            )
                        ], width="auto"),
                        dbc.Col([
                            dbc.Button(
                                "➕ Add Folder",
                                id="add-folder-toggle-button",
                                color="primary",
                                outline=True,
                                size="sm"
                            )
                        ], width="auto"),
                        dbc.Col([
                            dbc.Button(
                                "🔧 Filter Settings",
                                id="filter-toggle-button",
                                color="info",
                                outline=True,
                                size="sm"
                            )
                        ], width="auto"),
                    ], justify="start", className="mb-3"),
                ], style={"paddingBottom": "0"}),
                
                # Add Folder Collapse Section
                dbc.Collapse([
                    dbc.CardBody([
                        html.H6("📁 Add Custom Folder", className="text-primary mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Input(
                                    id="custom-folder-input",
                                    placeholder="Enter full path to project folder (e.g., D:\\Data\\QPU_Project)",
                                    type="text",
                                    size="sm"
                                ),
                            ], width=9),
                            dbc.Col([
                                dbc.Button(
                                    "Add",
                                    id="add-folder-button",
                                    color="success",
                                    size="sm",
                                    className="w-100"
                                ),
                            ], width=1),
                            dbc.Col([
                                dbc.Button(
                                "Disable All",  
                                id="clear-folders-button",
                                color="warning",  
                                size="sm",
                                className="w-100"
                                ),
                            ], width=2),
                        ], className="mb-3"),
                        html.Div(id="folder-add-feedback", className="mb-2"),
                        html.Hr(),
                        html.H6("📋 Currently Watching Folders:", className="text-info mb-3"),
                        html.Div([
                            dbc.Alert(
                                "💡 Tip: Custom folders are saved automatically and will persist across sessions. "
                                "Click the ❌ button next to any custom folder to remove it permanently.",
                                color="info",
                                dismissable=False,
                                className="py-2 small"
                            ),
                        ], className="mb-2"),
                        html.Div(id="watched-folders-list"),
                    ])
                ], id="add-folder-collapse", is_open=False),
                
                # Filter Settings Collapse Section
                dbc.Collapse([
                    dbc.CardBody([
                        html.H6("🔧 Experiment Filtering Configuration", className="text-info mb-3"),
                        dbc.Alert(
                            "📝 These filtering rules help categorize experiments correctly. "
                            "For example, 'resonator spectroscopy vs power' experiments are filtered out from "
                            "regular resonator spectroscopy because they are power analysis experiments.",
                            color="info",
                            dismissable=False,
                            className="py-2 small mb-3"
                        ),
                        
                        # Add New Experiment Type Section
                        dbc.Card([
                            dbc.CardHeader([
                                html.H6("➕ Add New Experiment Type", className="mb-0 text-success")
                            ]),
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label("Type ID (unique):", className="form-label small"),
                                        dbc.Input(
                                            id="new-exp-type-id",
                                            placeholder="e.g., custom_type",
                                            size="sm"
                                        ),
                                    ], md=3),
                                    dbc.Col([
                                        dbc.Label("Display Name:", className="form-label small"),
                                        dbc.Input(
                                            id="new-exp-title",
                                            placeholder="e.g., Custom Experiment",
                                            size="sm"
                                        ),
                                    ], md=3),
                                    dbc.Col([
                                        dbc.Label("Include Patterns (comma-separated):", className="form-label small"),
                                        dbc.Input(
                                            id="new-exp-patterns",
                                            placeholder="e.g., pattern1, pattern2",
                                            size="sm"
                                        ),
                                    ], md=4),
                                    dbc.Col([
                                        dbc.Label("Exclude Patterns (comma-separated):", className="form-label small"),
                                        dbc.Input(
                                            id="new-exp-exclude",
                                            placeholder="e.g., exclude1, exclude2",
                                            size="sm"
                                        ),
                                    ], md=2),
                                ], className="mb-2"),
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Button(
                                            "Add Experiment Type",
                                            id="add-exp-type-btn",
                                            color="success",
                                            size="sm"
                                        ),
                                    ], width="auto"),
                                    dbc.Col([
                                        html.Div(id="add-exp-feedback"),
                                    ]),
                                ]),
                            ])
                        ], className="mb-4"),
                        
                        # Existing Experiment Types Section
                        html.H6("🔧 Existing Experiment Types", className="text-primary mb-3"),
                        html.Div(id="filter-settings-content"),
                    ])
                ], id="filter-collapse", is_open=False),
                
                # Debug Information Collapse Section
                dbc.Collapse([
                    dbc.CardBody([
                        html.H6("📍 Path Information", className="text-info"),
                        html.P([
                            html.Strong("Current Working Directory: "), 
                            html.Code(os.getcwd(), style={"color": "#a8e6cf", "backgroundColor": "#2d2d2d"})
                        ]),
                        html.P([
                            html.Strong("BASE Path: "), 
                            html.Code(BASE, style={"color": "#a8e6cf", "backgroundColor": "#2d2d2d"})
                        ]),
                        html.P([
                            html.Strong("Default EXPERIMENT_BASE_PATH: "), 
                            html.Code(EXPERIMENT_BASE_PATH, style={"color": "#a8e6cf", "backgroundColor": "#2d2d2d"})
                        ]),
                        html.P([
                            html.Strong("Path Exists: "), 
                            html.Code(str(os.path.exists(EXPERIMENT_BASE_PATH)), style={"color": "#a8e6cf", "backgroundColor": "#2d2d2d"})
                        ]),
                        html.P([
                            html.Strong("Environment Variable: "), 
                            html.Code(os.environ.get("EXPERIMENT_BASE_PATH", "Not set"), style={"color": "#a8e6cf", "backgroundColor": "#2d2d2d"})
                        ]),
                        html.P([
                        html.Strong("os.path.isdir(): "), 
                        html.Code(str(os.path.isdir(EXPERIMENT_BASE_PATH)))
                        ]),
                        html.P([
                            html.Strong("os.access (readable): "), 
                            html.Code(str(os.access(EXPERIMENT_BASE_PATH, os.R_OK)) if os.path.exists(EXPERIMENT_BASE_PATH) else "Path not found")
                        ]),
                        html.P([
                            html.Strong("pathlib.Path.exists(): "), 
                            html.Code(str(Path(EXPERIMENT_BASE_PATH).exists()))
                        ]),
                        html.Hr(),
                        
                        html.H6("📂 Directory Explorer", className="text-info"),
                        dbc.Button(
                            "🔍 Explore Root Directory",
                            id="explore-root-button",
                            color="info",
                            outline=True,
                            size="sm",
                            className="mb-2"
                        ),
                        dbc.Collapse([
                            html.Pre(
                                "\n".join(get_directory_tree(BASE, max_depth=4)),
                                style={
                                    "backgroundColor": "#1e1e1e",
                                    "color": "#ffffff",
                                    "padding": "10px",
                                    "borderRadius": "5px",
                                    "fontSize": "12px",
                                    "maxHeight": "300px",
                                    "overflowY": "auto"
                                }
                            )
                        ], id="root-explore-collapse", is_open=False),
                        
                        dbc.Button(
                            "🔍 Explore Data Directory",
                            id="explore-data-button",
                            color="success",
                            outline=True,
                            size="sm",
                            className="mb-2"
                        ),
                        dbc.Collapse([
                            html.Pre(
                                "\n".join(get_directory_tree(os.path.join(BASE, "data"), max_depth=4)) if os.path.exists(os.path.join(BASE, "data")) else "❌ Data directory not found",
                                style={
                                    "backgroundColor": "#1e1e1e",
                                    "color": "#ffffff",
                                    "padding": "10px",
                                    "borderRadius": "5px",
                                    "fontSize": "12px",
                                    "maxHeight": "300px",
                                    "overflowY": "auto"
                                }
                            )
                        ], id="data-explore-collapse", is_open=False),
                    ])
                ], id="debug-collapse", is_open=False)
            ], className="mb-4"),
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("Experiment Selection"),
                        html.Div(id="experiment-count-info", className="mb-2 text-muted small"),
                        dbc.Row(                                             
                            [
                                dbc.Col(
                                    dcc.Dropdown(
                                        id="experiment-type-dropdown",
                                        placeholder="Select experiment type",
                                    ),
                                    md=6,
                                ),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id="experiment-folder-dropdown",
                                        placeholder="Select experiment folder",
                                        disabled=True,
                                    ),
                                    md=6,
                                ),
                            ],
                            className="g-2",
                        ),
                    ]
                ),
                className="mb-4",
            ),
            dbc.Row(dbc.Col(html.Div(id="experiment-content"))),
        ],
        fluid=True,
    )
])
# ────────────────────────────────────────────────────────────────────
# 3. Callbacks
# ────────────────────────────────────────────────────────────────────
# Clientside callback for theme switching
app.clientside_callback(
    """
    function(n_clicks, theme) {
        if (n_clicks > 0) {
            theme = theme === 'dark' ? 'light' : 'dark';
        }
        
        // Apply theme class to body
        if (theme === 'light') {
            document.body.classList.add('light-theme');
            document.querySelector('#theme-icon').textContent = '🌙';
        } else {
            document.body.classList.remove('light-theme');
            document.querySelector('#theme-icon').textContent = '☀️';
        }
        
        // Update all Plotly figures
        const figures = document.querySelectorAll('.js-plotly-plot');
        figures.forEach(fig => {
            if (fig.layout) {
                const template = theme === 'light' ? 'dashboard_light' : 'dashboard_dark';
                Plotly.relayout(fig, {'template': template});
            }
        });
        
        return theme;
    }
    """,
    Output("theme-store", "data"),
    Input("theme-toggle", "n_clicks"),
    State("theme-store", "data"),
)
# Update plotly template based on theme
@app.callback(
    Output("experiment-content", "style"),
    Input("theme-store", "data"),
)
def update_plotly_theme(theme):
    pio.templates.default = f"dashboard_{theme}"
    return {}
# New callback for Filter Settings toggle
@app.callback(
    Output("filter-collapse", "is_open"),
    Input("filter-toggle-button", "n_clicks"),
    State("filter-collapse", "is_open"),
)
def toggle_filter_settings(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# FIXED: Callback to manage experiment type updates (add new types and modify existing ones)
@app.callback(
    [Output("custom-experiment-types", "data"),
     Output("add-exp-feedback", "children"),
     Output("new-exp-type-id", "value"),
     Output("new-exp-title", "value"),
     Output("new-exp-patterns", "value"),
     Output("new-exp-exclude", "value"),
     Output("filter-update-trigger", "data")],
    [Input("add-exp-type-btn", "n_clicks"),
     Input({"type": "modify-exp-btn", "index": dash.dependencies.ALL}, "n_clicks"),
     Input({"type": "delete-exp-btn", "index": dash.dependencies.ALL}, "n_clicks"),
     Input({"type": "edit-patterns-input", "index": dash.dependencies.ALL}, "value"),
     Input({"type": "edit-exclude-input", "index": dash.dependencies.ALL}, "value"),
     Input({"type": "edit-title-input", "index": dash.dependencies.ALL}, "value")],
    [State("new-exp-type-id", "value"),
     State("new-exp-title", "value"),
     State("new-exp-patterns", "value"),
     State("new-exp-exclude", "value"),
     State("custom-experiment-types", "data"),
     State("filter-update-trigger", "data"),
     State({"type": "modify-exp-btn", "index": dash.dependencies.ALL}, "id"),
     State({"type": "delete-exp-btn", "index": dash.dependencies.ALL}, "id"),
     State({"type": "edit-patterns-input", "index": dash.dependencies.ALL}, "id"),
     State({"type": "edit-exclude-input", "index": dash.dependencies.ALL}, "id"),
     State({"type": "edit-title-input", "index": dash.dependencies.ALL}, "id")],
    prevent_initial_call=True
)
def manage_experiment_types(add_clicks, modify_clicks, delete_clicks, patterns_values, exclude_values, title_values,
                           new_id, new_title, new_patterns, new_exclude, custom_types, trigger,
                           modify_ids, delete_ids, patterns_ids, exclude_ids, title_ids):
    ctx = dash.callback_context
    if not ctx.triggered:
        return custom_types or {}, "", "", "", "", "", trigger or 0
    
    button_id = ctx.triggered[0]["prop_id"]
    custom_types = custom_types or {}
    trigger = trigger or 0
    
    # Handle adding new experiment type
    if "add-exp-type-btn" in button_id and add_clicks:
        if new_id and new_title and new_patterns:
            new_id = new_id.strip().lower().replace(" ", "_")
            new_title = new_title.strip()
            
            # Validate ID
            if new_id in DEFAULT_EXPERIMENT_MODULES or new_id in custom_types:
                return (
                    custom_types, 
                    dbc.Alert("Error: Experiment type ID already exists!", color="danger", dismissable=True, duration=3000), 
                    new_id, 
                    new_title, 
                    new_patterns, 
                    new_exclude or "", 
                    trigger
                )
            
            # Process patterns
            patterns = [p.strip() for p in new_patterns.split(",") if p.strip()]
            exclude_patterns = [p.strip() for p in (new_exclude or "").split(",") if p.strip()]
            
            # FIXED: Store only JSON-serializable data (no function references)
            custom_types[new_id] = {
                "title": new_title,
                "patterns": patterns,
                "exclude_patterns": exclude_patterns,
                "is_custom": True
                # NO layout_func or register_func here - they will be added when needed
            }
            
            # Update global experiment modules with functions
            update_experiment_modules_from_custom_types(custom_types)
            
            return (
                custom_types, 
                dbc.Alert(f"Added new experiment type: {new_title}", color="success", dismissable=True, duration=3000), 
                "",  # Clear input fields
                "", 
                "", 
                "", 
                trigger + 1
            )
    
    # Handle delete experiment type
    if "delete-exp-btn" in button_id and delete_ids and delete_clicks:
        for i, btn_id in enumerate(delete_ids):
            if i < len(delete_clicks) and delete_clicks[i] and delete_clicks[i] > 0:
                exp_id = btn_id["index"]
                if exp_id in custom_types:
                    del custom_types[exp_id]
                    # Update global experiment modules
                    update_experiment_modules_from_custom_types(custom_types)
                    return (
                        custom_types, 
                        dbc.Alert(f"Deleted experiment type: {exp_id}", color="warning", dismissable=True, duration=3000), 
                        "", 
                        "", 
                        "", 
                        "", 
                        trigger + 1
                    )
                break
    
    # Handle inline editing (patterns, exclude patterns, title)
    if any(["edit-patterns-input" in button_id, "edit-exclude-input" in button_id, "edit-title-input" in button_id]):
        # Update custom types based on inline edits
        for i, patterns_id in enumerate(patterns_ids or []):
            exp_id = patterns_id["index"]
            if i < len(patterns_values) and patterns_values[i] is not None:
                if exp_id in custom_types:
                    custom_types[exp_id]["patterns"] = [p.strip() for p in patterns_values[i].split(",") if p.strip()]
        
        for i, exclude_id in enumerate(exclude_ids or []):
            exp_id = exclude_id["index"]
            if i < len(exclude_values) and exclude_values[i] is not None:
                if exp_id in custom_types:
                    custom_types[exp_id]["exclude_patterns"] = [p.strip() for p in exclude_values[i].split(",") if p.strip()]
        
        for i, title_id in enumerate(title_ids or []):
            exp_id = title_id["index"]
            if i < len(title_values) and title_values[i] is not None:
                if exp_id in custom_types:
                    custom_types[exp_id]["title"] = title_values[i].strip()
        
        # Update global experiment modules with functions
        update_experiment_modules_from_custom_types(custom_types)
        
        return (
            custom_types, 
            dbc.Alert("Experiment type updated", color="info", dismissable=True, duration=2000), 
            "", 
            "", 
            "", 
            "", 
            trigger + 1
        )
    
    return custom_types or {}, "", "", "", "", "", trigger or 0

# FIXED: Callback to populate filter settings content
@app.callback(
    Output("filter-settings-content", "children"),
    [Input("filter-collapse", "is_open"),
     Input("custom-experiment-types", "data"),
     Input("filter-update-trigger", "data")],
)
def populate_filter_settings(is_open, custom_types, _):
    if not is_open:
        return ""
    
    # FIXED: Reconstruct modules with functions from the stored data
    update_experiment_modules_from_custom_types(custom_types or {})
    current_modules = get_experiment_modules()
    
    filter_items = []
    
    for exp_type, info in current_modules.items():
        patterns = info.get("patterns", [])
        exclude_patterns = info.get("exclude_patterns", [])
        is_custom = info.get("is_custom", False)
        
        # Create pattern display
        pattern_badges = [
            dbc.Badge(p, color="success", pill=True, className="me-1") 
            for p in patterns
        ]
        
        exclude_badges = [
            dbc.Badge(ep, color="danger", pill=True, className="me-1") 
            for ep in exclude_patterns
        ] if exclude_patterns else [
            dbc.Badge("None", color="secondary", pill=True, className="me-1")
        ]
        
        # Create editable inputs for custom types
        if is_custom:
            edit_content = [
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Title:", className="form-label small"),
                        dbc.Input(
                            id={"type": "edit-title-input", "index": exp_type},
                            value=info['title'],
                            size="sm"
                        ),
                    ], md=3),
                    dbc.Col([
                        dbc.Label("Include patterns:", className="form-label small"),
                        dbc.Input(
                            id={"type": "edit-patterns-input", "index": exp_type},
                            value=", ".join(patterns),
                            size="sm"
                        ),
                    ], md=4),
                    dbc.Col([
                        dbc.Label("Exclude patterns:", className="form-label small"),
                        dbc.Input(
                            id={"type": "edit-exclude-input", "index": exp_type},
                            value=", ".join(exclude_patterns),
                            size="sm"
                        ),
                    ], md=3),
                    dbc.Col([
                        dbc.Button(
                            "🗑️",
                            id={"type": "delete-exp-btn", "index": exp_type},
                            color="danger",
                            size="sm",
                            className="mt-4",
                            title="Delete this custom experiment type"
                        ),
                    ], md=2),
                ], className="mb-2")
            ]
        else:
            # Read-only display for default types
            edit_content = [
                html.Div([
                    html.Strong("Include patterns: ", className="text-success"),
                    html.Div(pattern_badges, className="d-inline")
                ], className="mb-2"),
                html.Div([
                    html.Strong("Exclude patterns: ", className="text-danger"),
                    html.Div(exclude_badges, className="d-inline")
                ], className="mb-2"),
                html.P(
                    f"Directories matching include patterns will be classified as {info['title']} "
                    f"unless they also match any exclude pattern.",
                    className="text-muted small mb-0"
                )
            ]
        
        # Card color based on type
        card_color = "warning" if is_custom else "light"
        
        filter_item = dbc.Card([
            dbc.CardBody([
                html.Div([
                    html.H6(f"{info['title']} ({exp_type})", className="text-primary mb-2 d-inline"),
                    dbc.Badge(
                        "CUSTOM" if is_custom else "DEFAULT", 
                        color="warning" if is_custom else "secondary", 
                        className="ms-2"
                    )
                ]),
                html.Div(edit_content)
            ])
        ], color=card_color, outline=True, className="mb-2")
        
        filter_items.append(filter_item)
    
    return html.Div([
        html.Div([
            dbc.Alert([
                html.Strong("How filtering works:"),
                html.Br(),
                "1. Directory names are checked against 'include patterns' for each experiment type",
                html.Br(),
                "2. If a match is found, the directory is then checked against 'exclude patterns'",
                html.Br(),
                "3. If any exclude pattern matches, the directory is filtered out from that experiment type",
                html.Br(),
                "4. This prevents misclassification (e.g., 'resonator vs power' → power analysis, not resonator spectroscopy)",
                html.Br(),
                html.Strong("Custom types can be edited inline - changes are saved automatically!")
            ], color="light", className="py-2 small mb-3"),
        ]),
        html.Div(filter_items)
    ])

# New callback for Add Folder toggle
@app.callback(
    Output("add-folder-collapse", "is_open"),
    Input("add-folder-toggle-button", "n_clicks"),
    State("add-folder-collapse", "is_open"),
)
def toggle_add_folder(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open
# Modified callback for adding/removing custom folders
@app.callback(
    [Output("additional-folders", "data"),
     Output("folder-add-feedback", "children"),
     Output("custom-folder-input", "value"),
     Output("disabled-folders", "data")],
    [Input("add-folder-button", "n_clicks"),
     Input("clear-folders-button", "n_clicks"),
     Input({"type": "folder-checkbox", "index": dash.dependencies.ALL}, "value"),
     Input({"type": "remove-folder-btn", "index": dash.dependencies.ALL}, "n_clicks")],
    [State("custom-folder-input", "value"),
     State("additional-folders", "data"),
     State("disabled-folders", "data"),
     State({"type": "folder-checkbox", "index": dash.dependencies.ALL}, "id"),
     State({"type": "remove-folder-btn", "index": dash.dependencies.ALL}, "id")],
)
def manage_custom_folders(add_clicks, clear_clicks, checkbox_values, remove_clicks, 
                         new_path, current_folders, disabled_folders, checkbox_ids, remove_btn_ids):
    ctx = dash.callback_context
    if not ctx.triggered:
        return current_folders or [], "", "", disabled_folders or []
    
    button_id = ctx.triggered[0]["prop_id"]
    
    # Handle remove button clicks
    if "remove-folder-btn" in button_id and remove_btn_ids:
        # Find which remove button was clicked
        for i, btn_id in enumerate(remove_btn_ids):
            if remove_clicks[i] and remove_clicks[i] > 0:
                folder_to_remove = btn_id["index"]
                # Remove from additional folders (can't remove default folder)
                if folder_to_remove in (current_folders or []):
                    updated_folders = [f for f in (current_folders or []) if f != folder_to_remove]
                    # Also remove from disabled list if it was there
                    updated_disabled = [f for f in (disabled_folders or []) if f != folder_to_remove]
                    return updated_folders, dbc.Alert(f"Removed folder: {folder_to_remove}", color="warning", dismissable=True, duration=3000), "", updated_disabled
                break
    
    # Handle checkbox toggle
    if "folder-checkbox" in button_id and checkbox_ids:
        # Create a mapping of folder paths to their checkbox states
        disabled_list = []
        for i, checkbox_id in enumerate(checkbox_ids):
            folder_path = checkbox_id["index"]
            # If checkbox is unchecked (False or empty list), add to disabled list
            if not checkbox_values[i]:
                disabled_list.append(folder_path)
        
        return current_folders or [], "", "", disabled_list
    
    # Handle clear all (now just disables all custom folders, doesn't remove them)
    if "clear-folders-button" in button_id:
        # Disable all folders (both default and custom)
        all_folders_to_disable = [EXPERIMENT_BASE_PATH] + (current_folders or [])
        return current_folders or [], dbc.Alert("All folders disabled! Check them to re-enable.", color="warning", dismissable=True, duration=3000), "", all_folders_to_disable
    
    # Handle add folder
    if "add-folder-button" in button_id and new_path:
        new_path = os.path.normpath(new_path.strip())
        
        # Validate the path
        if not os.path.exists(new_path):
            return current_folders or [], dbc.Alert(f"Path does not exist: {new_path}", color="danger", dismissable=True), new_path, disabled_folders or []
        
        if not os.path.isdir(new_path):
            return current_folders or [], dbc.Alert(f"Path is not a directory: {new_path}", color="danger", dismissable=True), new_path, disabled_folders or []
        
        # Check if already in list
        if new_path in (current_folders or []):
            # If it's disabled, enable it
            if new_path in (disabled_folders or []):
                updated_disabled = [f for f in (disabled_folders or []) if f != new_path]
                return current_folders, dbc.Alert(f"Path re-enabled: {new_path}", color="success", dismissable=True, duration=3000), "", updated_disabled
            else:
                return current_folders, dbc.Alert(f"Path already added and active: {new_path}", color="warning", dismissable=True), "", disabled_folders or []
        
        # Add to list
        updated_folders = (current_folders or []) + [new_path]
        return updated_folders, dbc.Alert(f"Successfully added: {new_path}", color="success", dismissable=True, duration=3000), "", disabled_folders or []
    
    return current_folders or [], "", "", disabled_folders or []
# Modified callback to display watched folders with remove buttons
@app.callback(
    Output("watched-folders-list", "children"),
    [Input("additional-folders", "data"),
     Input("disabled-folders", "data"),
     Input("folder-remove-trigger", "data")],
)
def display_watched_folders(additional_folders, disabled_folders, _):
    all_folders = [EXPERIMENT_BASE_PATH] + (additional_folders or [])
    disabled_folders = disabled_folders or []
    
    folder_items = []
    for i, folder in enumerate(all_folders):
        exists = os.path.exists(folder)
        is_disabled = folder in disabled_folders
        is_default = (i == 0)  # First item is always the default folder
        
        # Determine colors and icons based on state
        if not exists:
            color = "danger"
            icon = "❌"
            status_text = "Path not found"
        elif is_disabled:
            color = "secondary"
            icon = "⏸️"
            status_text = "Disabled"
        else:
            color = "success"
            icon = "✅"
            status_text = "Active"
        
        label = "Default" if is_default else f"Custom {i}"
        
        # Count experiments in this folder (only if exists and not disabled)
        exp_count = 0
        if exists and not is_disabled:
            folder_exps = find_experiments(folder)
            exp_count = sum(len(exps) for exps in folder_exps.values())
        
        # Create folder item with checkbox and optional remove button
        folder_content = [
            html.Div([
                html.Div([
                    dbc.Checklist(
                        id={"type": "folder-checkbox", "index": folder},
                        options=[{"label": "", "value": folder}],
                        value=[folder] if not is_disabled else [],
                        inline=True,
                        style={"marginRight": "10px"},
                        className="d-inline-block"
                    ),
                    html.Span(f"{icon} [{label}] ", className=f"text-{color} me-2"),
                    html.Code(folder, style={"fontSize": "11px"}),
                    html.Span(
                        f" ({exp_count} experiments)" if exp_count > 0 and not is_disabled else 
                        f" ({status_text})" if is_disabled or not exists else 
                        " (no experiments)", 
                        className="text-muted ms-2", 
                        style={"fontSize": "11px"}
                    ),
                ], className="flex-grow-1 d-flex align-items-center"),
                html.Div([
                    dbc.Badge(
                        "Default" if is_default else f"Custom {i}", 
                        color="primary" if is_default else "info", 
                        className="me-2", 
                        pill=True
                    ),
                    # Add remove button only for custom folders (not default)
                    dbc.Button(
                        "❌",
                        id={"type": "remove-folder-btn", "index": folder},
                        color="danger",
                        size="sm",
                        className="p-1",
                        style={"fontSize": "10px", "lineHeight": "1"},
                        title=f"Remove this custom folder"
                    ) if not is_default else None
                ], className="d-flex align-items-center")
            ], className="d-flex align-items-center justify-content-between")
        ]
        
        folder_items.append(
            dbc.ListGroupItem(
                folder_content, 
                className="py-2", 
                color="light" if not is_disabled else "secondary"
            )
        )
    
    # Add summary at the bottom
    total_folders = len(all_folders)
    custom_count = len(additional_folders or [])
    active_count = len([f for f in all_folders if f not in disabled_folders and os.path.exists(f)])
    disabled_count = len([f for f in all_folders if f in disabled_folders])
    
    summary = dbc.Alert(
        f"📊 Total: {total_folders} folder{'s' if total_folders != 1 else ''} | "
        f"✅ Active: {active_count} | "
        f"⏸️ Disabled: {disabled_count} | "
        f"(1 default + {custom_count} custom)",
        color="light",
        className="mt-3 py-2 small"
    )
    
    return html.Div([
        dbc.ListGroup(folder_items, flush=True),
        summary
    ])

# FIXED: Poll folders callback with proper module reconstruction
@app.callback(
    [Output("alert-container", "children"),
     Output("current-experiments", "data"),
     Output("experiment-count-info", "children")],
    [Input("folder-check-interval", "n_intervals"),
     Input("additional-folders", "data"),
     Input("disabled-folders", "data"),
     Input("filter-update-trigger", "data"),
     Input("custom-experiment-types", "data")],  # Added custom types as input
    State("current-experiments", "data"),
)
def poll_folders(_, additional_folders, disabled_folders, filter_trigger, custom_types, cur):
    # FIXED: Reconstruct modules with functions from the stored data
    update_experiment_modules_from_custom_types(custom_types or {})
    
    # Combine default path with additional folders
    all_paths = [EXPERIMENT_BASE_PATH] + (additional_folders or [])
    
    # Filter out disabled folders
    disabled_folders = disabled_folders or []
    active_paths = [p for p in all_paths if p not in disabled_folders]
    
    # Find experiments only from active paths (with enhanced filtering)
    new = find_experiments_multiple_paths(active_paths)
    
    # Count total experiments
    total_exp_count = sum(len(exps) for exps in new.values())
    active_folder_count = len([p for p in active_paths if os.path.exists(p)])
    total_folder_count = len(all_paths)
    disabled_count = len(disabled_folders)
    
    # Get current modules for display
    current_modules = get_experiment_modules()
    custom_count = len([info for info in current_modules.values() if info.get("is_custom", False)])
    
    count_info = html.Div([
        html.Span(f"Found {total_exp_count} experiments from {active_folder_count} active folder{'s' if active_folder_count != 1 else ''}"),
        html.Span(f" ({disabled_count} disabled)" if disabled_count > 0 else "", className="text-muted"),
        html.Br(),
        html.Span(f"🔧 Enhanced filtering active: {len(current_modules)} experiment types ({custom_count} custom)", className="text-info small")
    ])
    
    alert = None
    if cur:
        for typ, lst in new.items():
            added = {e["name"] for e in lst} - {e["name"] for e in cur.get(typ, [])}
            if added:
                current_modules = get_experiment_modules()
                type_title = current_modules.get(typ, {}).get('title', typ)
                alert = dbc.Alert(
                    f"New {type_title} experiment found: "
                    f"{', '.join(sorted(added))}",
                    color="info",
                    dismissable=True,
                    duration=10000,
                )
                break
    return alert, new, count_info

@app.callback(
    Output("debug-collapse", "is_open"),
    Input("debug-toggle-button", "n_clicks"),
    State("debug-collapse", "is_open"),
)
def toggle_debug_info(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open
@app.callback(
    Output("root-explore-collapse", "is_open"),
    Input("explore-root-button", "n_clicks"),
    State("root-explore-collapse", "is_open"),
)
def toggle_root_explore(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open
@app.callback(
    Output("data-explore-collapse", "is_open"),
    Input("explore-data-button", "n_clicks"),
    State("data-explore-collapse", "is_open"),
)
def toggle_data_explore(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# FIXED: Update type options with proper module reconstruction
@app.callback(
    [Output("experiment-type-dropdown", "options"),
     Output("experiment-type-dropdown", "value")],
    [Input("current-experiments", "modified_timestamp"),
     Input("filter-update-trigger", "data"),
     Input("custom-experiment-types", "data")],  # Added custom types as input
    State("current-experiments", "data"),
    State("experiment-type-dropdown", "value"),
)
def update_type_options(_, filter_trigger, custom_types, data, cur):
    if not data:
        return [], None
    
    # FIXED: Reconstruct modules with functions from the stored data
    update_experiment_modules_from_custom_types(custom_types or {})
    current_modules = get_experiment_modules()
    
    opts = [
        {
            "label": f"{current_modules.get(t, {}).get('title', t)} ({len(data.get(t, []))} items)",
            "value": t,
        }
        for t in data.keys()
        if t in current_modules
    ]
    return opts, cur if any(o["value"] == cur for o in opts) else None

@app.callback(
    [Output("experiment-folder-dropdown", "options"),
     Output("experiment-folder-dropdown", "disabled"),
     Output("experiment-folder-dropdown", "value")],
    Input("experiment-type-dropdown", "value"),
    State("current-experiments", "data"),
)
def update_folder_options(typ, data):
    if not typ or not data or typ not in data:
        return [], True, None
    
    # Enhanced labels showing which folder the experiment comes from
    opts = []
    for e in data[typ]:
        source = e.get("source_folder", "Unknown")
        # Shorten the source path for display
        if source == EXPERIMENT_BASE_PATH:
            source_label = "Default"
        else:
            source_label = f"...{source[-30:]}" if len(source) > 30 else source
        
        opts.append(dict(
            label=(
                f"{e['name']} ({e['date_folder']} – "
                f"{datetime.fromtimestamp(e['timestamp']).strftime('%H:%M:%S')}) "
                f"[{source_label}]"
            ),
            value=e["path"],
        ))
    
    return opts, False, None

# FIXED: Display experiment with proper module reconstruction
@app.callback(
    Output("experiment-content", "children"),
    [Input("experiment-folder-dropdown", "value"),
     Input("experiment-type-dropdown", "value"),
     Input("custom-experiment-types", "data")],  # Added custom types as input
)
def display_experiment(path, typ, custom_types):
    if not path or not typ:
        return html.Div(
            "Please select an experiment.",
            className="text-center text-muted mt-5",
        )
    
    # FIXED: Reconstruct modules with functions from the stored data
    update_experiment_modules_from_custom_types(custom_types or {})
    current_modules = get_experiment_modules()
    
    if typ in current_modules:
        layout_func = current_modules[typ].get("layout_func", create_generic_layout)
        return layout_func(path)
    else:
        return html.Div(
            f"Unknown experiment type: {typ}",
            className="text-center text-muted mt-5",
        )

# ────────────────────────────────────────────────────────────────────
# Register callbacks for each module
# ────────────────────────────────────────────────────────────────────
register_tof_callbacks(app)
register_res_callbacks(app)
register_qspec_callbacks(app)
register_prabi_callbacks(app)
register_t1_callbacks(app)
register_t2_echo_callbacks(app)
register_t2_ramsey_callbacks(app)
register_iq_blob_callbacks(app)
register_rpo_callbacks(app)
register_drag_callbacks(app)
register_rb_callbacks(app)
# ────────────────────────────────────────────────────────────────────
# 4. Run
# ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("[main] first scan:", find_experiments(EXPERIMENT_BASE_PATH))
    app.run(debug=True, port=7701)