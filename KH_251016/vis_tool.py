import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# =================================================================================
# Test Config 
# =================================================================================
con = "con1"
fem_1 = 1
res_out_fem = fem_1
res_out_port = 1
res_in_fem = fem_1
res_in_port = 1
q1_out_fem = fem_1
q1_out_port = 2

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                1: {
                    "type": "MW",
                    "analog_outputs": {
                        1: {"band": 2, "full_scale_power_dbm": -11, "upconverters": {1: {"frequency": 5500000000}}},
                        2: {"band": 3, "full_scale_power_dbm": 1, "upconverters": {1: {"frequency": 7000000000}}},
                        3: {"band": None, "full_scale_power_dbm": None, "upconverters": {1: {"frequency": None}}},
                        4: {"band": None, "full_scale_power_dbm": None, "upconverters": {1: {"frequency": None}}},
                        5: {"band": None, "full_scale_power_dbm": None, "upconverters": {1: {"frequency": None}}},
                        6: {"band": None, "full_scale_power_dbm": None, "upconverters": {1: {"frequency": None}}},
                        7: {"band": None, "full_scale_power_dbm": None, "upconverters": {1: {"frequency": None}}},
                        8: {"band": None, "full_scale_power_dbm": None, "upconverters": {1: {"frequency": None}}},
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {"band": 2, "downconverter_frequency": 5500000000, "gain_db": 0},
                        2: {"band": None, "downconverter_frequency": None, "gain_db": None},
                    },
                },
            },
        },
    },
    "elements": {
        "resonator": {
            "MWInput": {"port": ("con1", res_out_fem, res_out_port), "upconverter": 1},
            "intermediate_frequency": 60000000.0,
            "operations": {"cw": "const_pulse", "readout": "readout_pulse"},
            "MWOutput": {"port": ("con1", res_in_fem, res_in_port)},
            "time_of_flight": 28, "smearing": 0,
        },
        "qubit": {
            "MWInput": {"port": ("con1", q1_out_fem, q1_out_port), "upconverter": 1},
            "intermediate_frequency": 50000000.0,
            "operations": {"cw": "const_pulse", "saturation": "saturation_pulse"},
        },
    },
}
# =================================================================================

def visualize_opx1000_config(config, save_path=None):
    element_details = {}
    element_colors = {'resonator': '#fddab8', 'qubit': '#fff9b3'}
    element_labels = {'resonator': 'rr', 'qubit': 'xy'}

    # =========================
    # Layout Constants
    # =========================
    PANEL_WIDTH_RATIOS = [5.2, 2.7]  
    PANEL_WSPACE = 0.02 
    INFO_BOX_PAD = 0.35     

    num_slots = 8
    SLOT_WIDTH = 2.0                 
    SLOT_HEIGHT = 2.8
    SLOT_SPACING = 0.12               
    FRAME_PADDING = 0.1

    PORT_W = 0.90                    
    PORT_H = 0.22
    PORT_X_MARGIN = 0.50              
    OUT_PORT_Y_GAP = 0.12
    OUT_PORT_TOP_PAD = 0.22
    IN_STACK_FACTOR = 7.2             
    IN_PORT_TOP_PAD = 0.50

    for i, (el_name, el_props) in enumerate(config.get("elements", {}).items()):
        details = {}
        q_num = i + 1
        label_prefix = f"q{q_num}"
        details['label'] = f"{label_prefix}.{element_labels.get(el_name, el_name)}"

        if "MWInput" in el_props:
            con, fem, port = el_props["MWInput"]["port"]
            details.update({'out_fem': fem, 'out_port': port})
            fem_config = config["controllers"][con]["fems"][fem]
            port_config = fem_config["analog_outputs"][port]
            if port_config:
                details.update({
                    'if': el_props.get("intermediate_frequency", 0),
                    'lo': port_config.get("upconverters", {}).get(1, {}).get("frequency", 0),
                    'power': port_config.get("full_scale_power_dbm", 'N/A')
                })
                details['rf_freq'] = details.get('lo', 0) + details.get('if', 0)

        if "MWOutput" in el_props:
            con, fem, port = el_props["MWOutput"]["port"]
            details.update({'in_fem': fem, 'in_port': port})

        element_details[el_name] = details



    fig, (ax, ax_info) = plt.subplots(
        ncols=2,
        figsize=(18, 9),
        gridspec_kw={'width_ratios': PANEL_WIDTH_RATIOS, 'wspace': PANEL_WSPACE},
        facecolor='#f0f0f0'
    )
    fig.subplots_adjust(top=0.90, bottom=0.08, left=0.04, right=0.98)
    ax.axis('off')
    ax_info.axis('off')

    con = list(config["controllers"].keys())[0]  # 'con1'

    total_width = num_slots * SLOT_WIDTH + (num_slots - 1) * SLOT_SPACING
    opx_frame = patches.Rectangle(
        (-FRAME_PADDING, -0.2), total_width + 2*FRAME_PADDING, SLOT_HEIGHT + 0.4,
        linewidth=2, edgecolor='black', facecolor='lightgrey'
    )
    ax.add_patch(opx_frame)

    for i in range(num_slots):
        x_pos = i * (SLOT_WIDTH + SLOT_SPACING)
        slot_face_color = 'lightgrey' if (i+1) in config["controllers"][con]["fems"] else '#555555'
        slot = patches.Rectangle((x_pos, 0), SLOT_WIDTH, SLOT_HEIGHT,
                                 linewidth=1.5, edgecolor='black', facecolor=slot_face_color)
        ax.add_patch(slot)
        ax.text(x_pos + SLOT_WIDTH / 2, -0.1, f"Slot {i+1}", ha='center', va='center', fontsize=11)

    used_fems = {details.get(k) for details in element_details.values() for k in ['out_fem', 'in_fem']}

    for fem_id in filter(None, used_fems):
        fem_x_start = (fem_id - 1) * (SLOT_WIDTH + SLOT_SPACING)

        fem_elements_out = {
            details['out_port']: (details['label'], element_colors.get(el_name, 'pink'))
            for el_name, details in element_details.items() if details.get('out_fem') == fem_id
        }
        fem_elements_in = {
            details['in_port']: (details['label'], element_colors.get(el_name, 'pink'))
            for el_name, details in element_details.items() if details.get('in_fem') == fem_id
        }

        out_x = fem_x_start + PORT_X_MARGIN
        in_x = fem_x_start + SLOT_WIDTH - PORT_X_MARGIN

        for i in range(8):
            port_num = i + 1
            y = SLOT_HEIGHT - (i * (PORT_H + OUT_PORT_Y_GAP) + OUT_PORT_TOP_PAD)
            face_color = 'white'
            label = None
            if port_num in fem_elements_out:
                label, face_color = fem_elements_out[port_num]

            ellipse = patches.Ellipse((out_x, y), PORT_W, PORT_H, facecolor=face_color, edgecolor='black', lw=1.2)
            ax.add_patch(ellipse)

            if label:
                ax.text(out_x, y + PORT_H * 0.25, str(port_num), ha='center', va='center', fontsize=9, fontweight='bold')
                ax.text(out_x, y - PORT_H * 0.25, label, ha='center', va='center', fontsize=8, fontweight='bold')
            else:
                ax.text(out_x, y, str(port_num), ha='center', va='center', fontsize=9)

        for i in range(2):
            port_num = i + 1
            y = SLOT_HEIGHT - (i * (PORT_H * IN_STACK_FACTOR) + IN_PORT_TOP_PAD)
            face_color = 'white'
            label = None
            if port_num in fem_elements_in:
                label, face_color = fem_elements_in[port_num]

            ellipse = patches.Ellipse((in_x, y), PORT_W, PORT_H, facecolor=face_color, edgecolor='black', lw=1.2)
            ax.add_patch(ellipse)

            if label:
                ax.text(in_x, y + PORT_H * 0.25, str(port_num), ha='center', va='center', fontsize=9, fontweight='bold')
                ax.text(in_x, y - PORT_H * 0.25, label, ha='center', va='center', fontsize=8, fontweight='bold')
            else:
                ax.text(in_x, y, str(port_num), ha='center', va='center', fontsize=9)

    # Titles
    fig.suptitle('QM Instrument Config', fontsize=22, y=0.98)
    ax.set_title('OPX1000 #1 with MW-FEM', fontsize=14, loc='left', y=1.02)

    # Axis limits only for LEFT axis
    ax.set_xlim(-FRAME_PADDING - 0.1, total_width + FRAME_PADDING + 0.1)
    ax.set_ylim(-0.2, SLOT_HEIGHT + 0.2)

    # -------------------------
    # Build "Element Details" text and draw on RIGHT axis
    # -------------------------
    info_text_lines = ["Element Details", "="*55]
    element_keys = list(element_details.keys())

    for i, el_name in enumerate(element_keys):
        details = element_details[el_name]
        rf_ghz = (details.get('rf_freq', 0) or 0) / 1e9
        lo_ghz = (details.get('lo', 0) or 0) / 1e9
        if_mhz = (details.get('if', 0) or 0) / 1e6
        power_dbm = details.get('power', 'N/A')

        port_info = f"(FEM {details.get('out_fem', 'N/A')}, Out {details.get('out_port', 'N/A')}"
        if 'in_port' in details:
            port_info += f", In {details.get('in_port', 'N/A')}"
        port_info += ")"

        info_text_lines.append(f"{details['label']} ({el_name})")
        info_text_lines.append(f"  {'• Port':<12}: {port_info}")
        info_text_lines.append(f"  {'• RF Freq':<12}: {rf_ghz:.3f} GHz")
        info_text_lines.append(f"    {' ':<12}  (LO: {lo_ghz:.3f} GHz, IF: {if_mhz:.1f} MHz)")
        info_text_lines.append(f"  {'• Power':<12}: {power_dbm} dBm")
        if i < len(element_keys) - 1:
            info_text_lines.append("")

    info_text = "\n".join(info_text_lines)

    ax_info.text(
        0.01, 0.98, info_text,              
        transform=ax_info.transAxes,
        ha='left', va='top',
        fontfamily='DejaVu Sans Mono', fontsize=12, linespacing=1.25,
        bbox=dict(boxstyle='round,pad={}'.format(INFO_BOX_PAD), fc='white', ec='black')
    )

    # Save / show
    if save_path:
        try:
            p = Path(save_path)
            p.parent.mkdir(parents=True, exist_ok=True)
            plt.savefig(p, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
            print(f"✅ Plot saved to: {p.resolve()}")
        except Exception as e:
            print(f"❌ Failed to save plot: {e}")

    plt.show()

if __name__ == "__main__":
    visualize_opx1000_config(config, save_path="./opx1000_config_final.png")