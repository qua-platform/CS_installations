# theme.py  –  registers project-wide Plotly templates
import plotly.io as pio
from plotly import graph_objects as go

# ────────────────────────────────────────────────────────────────────
# Dark theme template
# ────────────────────────────────────────────────────────────────────
dashboard_dark = go.layout.Template(
    layout=dict(
        paper_bgcolor="#2A2A2C",      # Card color (outer frame)
        plot_bgcolor="#1E1E1E",       # Dark interior
        font=dict(color="#E0E0E0", size=14, family="Segoe UI, Arial, sans-serif"),
        legend=dict(bgcolor="#2A2A2C", font=dict(color="#E0E0E0")),
        xaxis=dict(
            gridcolor="#555555",
            zerolinecolor="#555555",
            tickfont=dict(color="#E0E0E0"),
            title_font=dict(color="#E0E0E0")
        ),
        yaxis=dict(
            gridcolor="#555555",
            zerolinecolor="#555555",
            tickfont=dict(color="#E0E0E0"),
            title_font=dict(color="#E0E0E0")
        ),
        coloraxis=dict(
            colorbar=dict(
                tickfont=dict(color="#E0E0E0"),
                title_font=dict(color="#E0E0E0")
            )
        ),
        title=dict(font=dict(color="#E0E0E0"))
    )
)

# ────────────────────────────────────────────────────────────────────
# Light theme template (updated for clean white background)
# ────────────────────────────────────────────────────────────────────
dashboard_light = go.layout.Template(
    layout=dict(
        paper_bgcolor="#FFFFFF",      # White background for cards & page
        plot_bgcolor="#FFFFFF",       # White interior to match
        font=dict(color="#333333", size=14, family="Segoe UI, Arial, sans-serif"),
        legend=dict(bgcolor="#FFFFFF", font=dict(color="#333333")),
        xaxis=dict(
            gridcolor="#DDDDDD",      # Soft, light-gray grid lines
            zerolinecolor="#CCCCCC",
            tickfont=dict(color="#333333"),
            title_font=dict(color="#333333")
        ),
        yaxis=dict(
            gridcolor="#DDDDDD",
            zerolinecolor="#CCCCCC",
            tickfont=dict(color="#333333"),
            title_font=dict(color="#333333")
        ),
        coloraxis=dict(
            colorbar=dict(
                tickfont=dict(color="#333333"),
                title_font=dict(color="#333333"),
                outlinecolor="#CCCCCC",
                outlinewidth=1
            )
        ),
        title=dict(font=dict(color="#333333"))
    )
)

# ────────────────────────────────────────────────────────────────────
# Register both templates
# ────────────────────────────────────────────────────────────────────
pio.templates["dashboard_dark"] = dashboard_dark
pio.templates["dashboard_light"] = dashboard_light

# Default to dark theme
pio.templates.default = "dashboard_dark"
