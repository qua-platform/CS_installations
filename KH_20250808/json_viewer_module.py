import dash
from dash import dcc, html, Input, Output, State, MATCH, ALL, ctx
import dash_bootstrap_components as dbc
import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
import uuid
import re

class JsonViewerModule:
    """
    Enhanced JSON viewer with search, copy, edit, and save features.
    """
    
    @staticmethod
    def highlight_search_term(text: str, search_term: str) -> html.Span:
        """
        Highlight search terms in text.
        """
        if not search_term:
            return text
        
        # Case-insensitive search
        pattern = re.compile(re.escape(search_term), re.IGNORECASE)
        parts = pattern.split(text)
        matches = pattern.findall(text)
        
        result = []
        for i, part in enumerate(parts):
            result.append(part)
            if i < len(matches):
                result.append(html.Mark(matches[i], style={"backgroundColor": "yellow"}))
        
        return html.Span(result)
    
    @staticmethod
    def search_json_tree(data: Any, search_term: str, path: str = "") -> List[str]:
        """
        Search for a term in JSON data and return paths to matching nodes.
        """
        matches = []
        search_lower = search_term.lower()
        
        if isinstance(data, dict):
            for key, value in data.items():
                current_path = f"{path}.{key}" if path else key
                if search_lower in str(key).lower() or search_lower in str(value).lower():
                    matches.append(current_path)
                matches.extend(JsonViewerModule.search_json_tree(value, search_term, current_path))
        
        elif isinstance(data, list):
            for i, item in enumerate(data):
                current_path = f"{path}[{i}]"
                if search_lower in str(item).lower():
                    matches.append(current_path)
                matches.extend(JsonViewerModule.search_json_tree(item, search_term, current_path))
        
        else:
            if search_lower in str(data).lower():
                matches.append(path)
        
        return matches
    
    @staticmethod
    def get_value_at_path(data: Any, path: str) -> Any:
        """
        Get value from JSON data at a specific path.
        """
        if not path:
            return data
        
        parts = path.replace('[', '.').replace(']', '').split('.')
        current = data
        
        for part in parts:
            if part == '':
                continue
            try:
                if isinstance(current, list):
                    current = current[int(part)]
                else:
                    current = current[part]
            except (KeyError, IndexError, ValueError):
                return None
        
        return current
    
    @staticmethod
    def create_json_viewer_panel(folder_path: str, panel_id: str = None) -> html.Div:
        """
        Create the complete enhanced JSON viewer interface.
        """
        if panel_id is None:
            panel_id = str(uuid.uuid4())
        
        # Find all JSON files
        json_files = {}
        base_path = Path(folder_path)
        
        try:
            for json_path in base_path.rglob("*.json"):
                rel_path = json_path.relative_to(base_path)
                display_name = str(rel_path)
                json_files[display_name] = str(json_path)
        except Exception as e:
            return dbc.Alert(f"Error scanning JSON files: {e}", color="danger")
        
        if not json_files:
            return dbc.Alert("No JSON files found in this folder", color="info")
        
        # Create tabs for each file
        tabs = []
        for idx, (name, path) in enumerate(json_files.items()):
            tabs.append(
                dbc.Tab(
                    label=name if len(name) <= 30 else name[:27] + "...",
                    tab_id=f"json-tab-{panel_id}-{idx}",
                    label_style={"fontSize": "0.9em"}
                )
            )
        
        return html.Div([
            html.H6("JSON File Viewer", className="mb-3"),
            
            # Store JSON files info
            dcc.Store(
                id={"type": "json-files-store", "panel": panel_id},
                data={"files": json_files, "current_idx": 0}
            ),
            
            # Store for current file data
            dcc.Store(id={"type": "json-current-data", "panel": panel_id}),
            
            # Store for edit state
            dcc.Store(
                id={"type": "json-edit-state", "panel": panel_id},
                data={"editing": False, "modified": False}
            ),
            
            # Tabs
            dbc.Tabs(
                tabs,
                id={"type": "json-file-tabs", "panel": panel_id},
                active_tab=f"json-tab-{panel_id}-0" if tabs else None
            ),
            
            # Content area
            html.Div(
                id={"type": "json-viewer-content", "panel": panel_id},
                style={"marginTop": "15px"}
            ),
            
            # Modal for save dialog
            dbc.Modal([
                dbc.ModalHeader("Save JSON File"),
                dbc.ModalBody([
                    dbc.Label("Enter filename:"),
                    dbc.Input(
                        id={"type": "json-save-filename", "panel": panel_id},
                        placeholder="filename.json",
                        value=""
                    ),
                    html.Small(
                        "File will be saved in the same directory as the original",
                        className="text-muted"
                    )
                ]),
                dbc.ModalFooter([
                    dbc.Button(
                        "Cancel",
                        id={"type": "json-save-cancel", "panel": panel_id},
                        color="secondary"
                    ),
                    dbc.Button(
                        "Save",
                        id={"type": "json-save-confirm", "panel": panel_id},
                        color="primary"
                    )
                ])
            ], id={"type": "json-save-modal", "panel": panel_id}, is_open=False),
            
            # Toast for notifications
            dbc.Toast(
                "Operation completed",
                id={"type": "json-toast", "panel": panel_id},
                header="Notification",
                is_open=False,
                dismissable=True,
                duration=3000,
                icon="success",
                style={"position": "fixed", "top": 66, "right": 10, "width": 350}
            )
        ])
    
    @staticmethod
    def create_json_tree_view(json_data: Any, search_term: str = "", panel_id: str = "") -> html.Div:
        """
        Create the tree view for JSON data with search highlighting.
        """
        
        def build_node(key: str, value: Any, path: List[str], level: int = 0) -> html.Div:
            current_path = ".".join(path + [str(key)] if key else path)
            indent = level * 20
            
            # Check if this node matches search
            is_match = False
            if search_term:
                if search_term.lower() in str(key).lower() or search_term.lower() in json.dumps(value).lower():
                    is_match = True
            
            node_style = {
                "backgroundColor": "rgba(255, 255, 0, 0.2)" if is_match else "transparent",
                "borderRadius": "3px",
                "padding": "2px"
            }
            
            if isinstance(value, dict):
                return html.Div([
                    html.Div([
                        html.Button(
                            "▼",
                            id={"type": "tree-toggle", "path": current_path, "panel": panel_id},
                            style={"border": "none", "background": "none", "cursor": "pointer"},
                            className="tree-toggle"
                        ),
                        dcc.Clipboard(
                            target_id={"type": "tree-node-data", "path": current_path, "panel": panel_id},
                            title="Copy this section",
                            style={"display": "inline-block", "marginLeft": "5px", "cursor": "pointer"}
                        ),
                        html.Span(
                            JsonViewerModule.highlight_search_term(f"{key}: " if key else "", search_term),
                            style={"fontWeight": "bold", "color": "#0066cc"}
                        ),
                        html.Span("{...}", style={"color": "#666"}),
                        html.Span(
                            json.dumps(value),
                            id={"type": "tree-node-data", "path": current_path, "panel": panel_id},
                            style={"display": "none"}
                        )
                    ], style={"paddingLeft": f"{indent}px", **node_style}),
                    html.Div(
                        [build_node(k, v, path + [str(key)] if key else path, level + 1) 
                         for k, v in value.items()],
                        id={"type": "tree-children", "path": current_path, "panel": panel_id},
                        style={"display": "block"}
                    )
                ])
            
            elif isinstance(value, list):
                return html.Div([
                    html.Div([
                        html.Button(
                            "▼",
                            id={"type": "tree-toggle", "path": current_path, "panel": panel_id},
                            style={"border": "none", "background": "none", "cursor": "pointer"},
                            className="tree-toggle"
                        ),
                        dcc.Clipboard(
                            target_id={"type": "tree-node-data", "path": current_path, "panel": panel_id},
                            title="Copy this section",
                            style={"display": "inline-block", "marginLeft": "5px", "cursor": "pointer"}
                        ),
                        html.Span(
                            JsonViewerModule.highlight_search_term(f"{key}: " if key else "", search_term),
                            style={"fontWeight": "bold", "color": "#0066cc"}
                        ),
                        html.Span(f"[{len(value)} items]", style={"color": "#666"}),
                        html.Span(
                            json.dumps(value),
                            id={"type": "tree-node-data", "path": current_path, "panel": panel_id},
                            style={"display": "none"}
                        )
                    ], style={"paddingLeft": f"{indent}px", **node_style}),
                    html.Div(
                        [build_node(f"[{i}]", v, path + [str(key)] if key else path, level + 1) 
                         for i, v in enumerate(value)],
                        id={"type": "tree-children", "path": current_path, "panel": panel_id},
                        style={"display": "block"}
                    )
                ])
            
            else:
                value_str = json.dumps(value)
                value_color = "#008000" if isinstance(value, str) else "#ff6600" if isinstance(value, (int, float)) else "#666"
                
                return html.Div([
                    html.Span(
                        JsonViewerModule.highlight_search_term(f"{key}: " if key else "", search_term),
                        style={"fontWeight": "bold", "color": "#0066cc", "paddingLeft": f"{indent}px"}
                    ),
                    html.Span(
                        JsonViewerModule.highlight_search_term(value_str, search_term),
                        style={"color": value_color}
                    ),
                    dcc.Clipboard(
                        target_id={"type": "leaf-value", "path": current_path, "panel": panel_id},
                        title="Copy value",
                        style={"display": "inline-block", "marginLeft": "5px", "cursor": "pointer"}
                    ),
                    html.Span(
                        value_str,
                        id={"type": "leaf-value", "path": current_path, "panel": panel_id},
                        style={"display": "none"}
                    )
                ], style=node_style)
        
        return html.Div(
            build_node("", json_data, [], 0),
            style={
                "fontFamily": "monospace",
                "fontSize": "0.9em",
                "lineHeight": "1.6",
                "padding": "10px",
                "backgroundColor": "#f8f9fa",
                "border": "1px solid #dee2e6",
                "borderRadius": "4px",
                "maxHeight": "500px",
                "overflowY": "auto"
            }
        )
    
    @staticmethod
    def register_callbacks(app):  # <-- CORRECTED METHOD NAME
        """
        Register all callbacks for the enhanced JSON viewer.
        """
        
        # Load JSON file content when tab changes
        @app.callback(
            Output({"type": "json-viewer-content", "panel": MATCH}, "children"),
            Output({"type": "json-current-data", "panel": MATCH}, "data"),
            Output({"type": "json-save-filename", "panel": MATCH}, "value"),
            Input({"type": "json-file-tabs", "panel": MATCH}, "active_tab"),
            State({"type": "json-files-store", "panel": MATCH}, "data"),
            prevent_initial_call=False
        )
        def load_json_file(active_tab, files_store):
            if not active_tab or not files_store:
                return dash.no_update, dash.no_update, dash.no_update
            
            # Extract index from tab id
            try:
                idx = int(active_tab.split('-')[-1])
                file_list = list(files_store["files"].items())
                if idx >= len(file_list):
                    return dash.no_update, dash.no_update, dash.no_update
                
                display_name, file_path = file_list[idx]
                
                # Load JSON data
                with open(file_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # Extract panel_id from triggered_id
                panel_id = ctx.triggered_id["panel"] if ctx.triggered_id else ""
                
                # Suggest new filename
                base_name = Path(file_path).stem
                suggested_name = f"{base_name}_modified.json"
                
                # Create viewer content
                content = html.Div([
                    # Search bar
                    dbc.InputGroup([
                        dbc.Input(
                            id={"type": "json-search-input", "panel": panel_id},
                            placeholder="Search in JSON...",
                            type="text",
                            debounce=True
                        ),
                        dbc.Button(
                            "Clear",
                            id={"type": "json-search-clear", "panel": panel_id},
                            color="secondary",
                            outline=True
                        )
                    ], size="sm", className="mb-3"),
                    
                    # Control buttons
                    dbc.ButtonGroup([
                        dbc.Button(
                            "Expand All",
                            id={"type": "json-expand-all", "panel": panel_id},
                            color="info",
                            size="sm",
                            outline=True
                        ),
                        dbc.Button(
                            "Collapse All",
                            id={"type": "json-collapse-all", "panel": panel_id},
                            color="info",
                            size="sm",
                            outline=True
                        ),
                        dbc.Button(
                            "Edit JSON",
                            id={"type": "json-edit-toggle", "panel": panel_id},
                            color="primary",
                            size="sm",
                            outline=True
                        ),
                        dbc.Button(
                            "Save As...",
                            id={"type": "json-save-btn", "panel": panel_id},
                            color="success",
                            size="sm",
                            outline=True,
                            disabled=True
                        )
                    ], size="sm", className="mb-3"),
                    
                    # Tree view (default)
                    html.Div(
                        JsonViewerModule.create_json_tree_view(json_data, "", panel_id),
                        id={"type": "json-tree-container", "panel": panel_id}
                    ),
                    
                    # Editor (hidden initially)
                    dbc.Textarea(
                        id={"type": "json-editor-textarea", "panel": panel_id},
                        value=json.dumps(json_data, indent=2),
                        style={
                            "display": "none",
                            "fontFamily": "monospace",
                            "fontSize": "0.9em",
                            "height": "500px",
                            "width": "100%"
                        }
                    )
                ])
                
                return content, {"data": json_data, "path": file_path}, suggested_name
                
            except Exception as e:
                return dbc.Alert(f"Error loading file: {e}", color="danger"), {}, ""
        
        # Toggle between tree view and editor
        @app.callback(
            Output({"type": "json-tree-container", "panel": MATCH}, "style"),
            Output({"type": "json-editor-textarea", "panel": MATCH}, "style"),
            Output({"type": "json-edit-toggle", "panel": MATCH}, "children"),
            Output({"type": "json-save-btn", "panel": MATCH}, "disabled"),
            Output({"type": "json-edit-state", "panel": MATCH}, "data"),
            Input({"type": "json-edit-toggle", "panel": MATCH}, "n_clicks"),
            State({"type": "json-edit-state", "panel": MATCH}, "data"),
            prevent_initial_call=True
        )
        def toggle_edit_mode(n_clicks, edit_state):
            if not n_clicks:
                return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
            
            editing = edit_state.get("editing", False)
            
            if editing:
                # Switch to view mode
                return (
                    {"display": "block"},
                    {"display": "none", "fontFamily": "monospace", "fontSize": "0.9em", 
                     "height": "500px", "width": "100%"},
                    "Edit JSON",
                    True,
                    {"editing": False, "modified": edit_state.get("modified", False)}
                )
            else:
                # Switch to edit mode
                return (
                    {"display": "none"},
                    {"display": "block", "fontFamily": "monospace", "fontSize": "0.9em",
                     "height": "500px", "width": "100%"},
                    "View Tree",
                    False,
                    {"editing": True, "modified": False}
                )
        
        # Search functionality
        @app.callback(
            Output({"type": "json-tree-container", "panel": MATCH}, "children"),
            Input({"type": "json-search-input", "panel": MATCH}, "value"),
            Input({"type": "json-search-clear", "panel": MATCH}, "n_clicks"),
            State({"type": "json-current-data", "panel": MATCH}, "data"),
            prevent_initial_call=True
        )
        def search_json(search_term, clear_clicks, current_data):
            triggered = ctx.triggered_id
            panel_id = triggered["panel"] if triggered else ""
            
            if triggered and triggered["type"] == "json-search-clear":
                search_term = ""
            
            if current_data and "data" in current_data:
                return JsonViewerModule.create_json_tree_view(
                    current_data["data"], 
                    search_term or "", 
                    panel_id
                )
            
            return dash.no_update
        
        # Expand/Collapse all
        @app.callback(
            Output({"type": "tree-children", "path": ALL, "panel": MATCH}, "style"),
            Output({"type": "tree-toggle", "path": ALL, "panel": MATCH}, "children"),
            Input({"type": "json-expand-all", "panel": MATCH}, "n_clicks"),
            Input({"type": "json-collapse-all", "panel": MATCH}, "n_clicks"),
            State({"type": "tree-children", "path": ALL, "panel": MATCH}, "id"),
            prevent_initial_call=True
        )
        def expand_collapse_all(expand_clicks, collapse_clicks, children_ids):
            triggered = ctx.triggered_id
            
            if not triggered:
                return dash.no_update, dash.no_update
            
            num_nodes = len(children_ids)
            
            if triggered["type"] == "json-expand-all":
                return [{"display": "block"}] * num_nodes, ["▼"] * num_nodes
            else:
                return [{"display": "none"}] * num_nodes, ["▶"] * num_nodes
        
        # Individual node toggle
        @app.callback(
            Output({"type": "tree-children", "path": MATCH, "panel": MATCH}, "style"),
            Output({"type": "tree-toggle", "path": MATCH, "panel": MATCH}, "children"),
            Input({"type": "tree-toggle", "path": MATCH, "panel": MATCH}, "n_clicks"),
            State({"type": "tree-children", "path": MATCH, "panel": MATCH}, "style"),
            prevent_initial_call=True
        )
        def toggle_node(n_clicks, current_style):
            if n_clicks:
                is_visible = current_style.get("display") != "none"
                if is_visible:
                    return {"display": "none"}, "▶"
                else:
                    return {"display": "block"}, "▼"
            return dash.no_update, dash.no_update
        
        # Open save modal
        @app.callback(
            Output({"type": "json-save-modal", "panel": MATCH}, "is_open"),
            Input({"type": "json-save-btn", "panel": MATCH}, "n_clicks"),
            Input({"type": "json-save-cancel", "panel": MATCH}, "n_clicks"),
            Input({"type": "json-save-confirm", "panel": MATCH}, "n_clicks"),
            State({"type": "json-save-modal", "panel": MATCH}, "is_open"),
            prevent_initial_call=True
        )
        def toggle_save_modal(save_clicks, cancel_clicks, confirm_clicks, is_open):
            triggered = ctx.triggered_id
            
            if triggered and triggered["type"] == "json-save-btn":
                return True
            elif triggered and triggered["type"] in ["json-save-cancel", "json-save-confirm"]:
                return False
            
            return is_open
        
        # Save file
        @app.callback(
            Output({"type": "json-toast", "panel": MATCH}, "children"),
            Output({"type": "json-toast", "panel": MATCH}, "is_open"),
            Output({"type": "json-toast", "panel": MATCH}, "icon"),
            Input({"type": "json-save-confirm", "panel": MATCH}, "n_clicks"),
            State({"type": "json-save-filename", "panel": MATCH}, "value"),
            State({"type": "json-editor-textarea", "panel": MATCH}, "value"),
            State({"type": "json-current-data", "panel": MATCH}, "data"),
            prevent_initial_call=True
        )
        def save_json_file(n_clicks, filename, editor_content, current_data):
            if not n_clicks or not filename or not current_data:
                return dash.no_update, dash.no_update, dash.no_update
            
            try:
                # Parse the JSON to validate it
                json_data = json.loads(editor_content)
                
                # Get the directory of the original file
                original_path = Path(current_data["path"])
                save_dir = original_path.parent
                
                # Ensure filename has .json extension
                if not filename.endswith('.json'):
                    filename += '.json'
                
                # Create full save path
                save_path = save_dir / filename
                
                # Save the file
                with open(save_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, indent=2)
                
                return f"File saved successfully as {filename}", True, "success"
                
            except json.JSONDecodeError as e:
                return f"Invalid JSON: {str(e)}", True, "danger"
            except Exception as e:
                return f"Error saving file: {str(e)}", True, "danger"

# Add CSS styling
json_viewer_css = """
.json-node:hover {
    background-color: rgba(0, 123, 255, 0.05);
}

.json-toggle-btn:hover, .json-copy-btn:hover {
    background-color: rgba(0, 123, 255, 0.1) !important;
    border-radius: 3px;
}

.json-search-highlight {
    background-color: yellow;
    font-weight: bold;
}
"""