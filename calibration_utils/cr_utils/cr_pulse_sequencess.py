from typing import Optional, Literal

import numpy as np
from qm.qua import *

from quam_builder.architecture.superconducting.qubit import AnyTransmon
from quam_builder.architecture.superconducting.qubit_pair import AnyTransmonPair
from quam_builder.architecture.superconducting.components.cross_resonance import CrossResonanceMW, CrossResonanceIQ
from qm.qua._dsl import QuaExpression, QuaVariable

qua_T = QuaVariable | QuaExpression

def play_cross_resonance(
    qc: AnyTransmon, 
    qt: AnyTransmon,
    cr: CrossResonanceMW | CrossResonanceIQ,
    cr_type: Literal["direct", "direct+cancel", "direct+echo", "direct+cancel+echo"] = "direct",
    cr_drive_amp_scaling: float |qua_T = 1.0,
    cr_drive_phase: float | qua_T = 1.0,
    cr_cancel_amp_scaling: float | qua_T = 0.0,
    cr_cancel_phase: float | qua_T = 0.0,
):
    elems = [qc.xy.name, qt.xy.name, cr.name]

    if cr_type == "direct":
        # phase shift for cr drive
        cr.frame_rotation_2pi(cr_drive_phase)
        align(*elems)
        cr.play("square", amplitude_scale=cr_drive_amp_scaling)
        align(*elems)
        reset_frame(cr.name)

    elif cr_type == "direct+echo":
        # phase shift for cr drive
        cr.frame_rotation_2pi(cr_drive_phase)
        qt.xy.frame_rotation_2pi(cr_cancel_phase)
        # direct + cancel
        align(*elems)
        cr.play("square", amplitude_scale=cr_drive_amp_scaling)
        # pi pulse on control
        align(*elems)
        qc.xy.play("x180")
        # echoed direct + cancel
        align(*elems)
        cr.play("square", amplitude_scale=-cr_drive_amp_scaling)
        # pi pulse on control
        align(*elems)
        qc.xy.play("x180")
        # align for the next step and clear the phase shift
        align(*elems)
        reset_frame(cr.name)
        reset_frame(qt.xy.name)

    elif cr_type == "direct+cancel":
        # phase shift for cr drive
        cr.frame_rotation_2pi(cr_drive_phase)
        qt.xy.frame_rotation_2pi(cr_cancel_phase)
        # direct + cancel
        align(*elems)
        cr.play("square", amplitude_scale=cr_drive_amp_scaling)
        qt.xy.play(f"{cr.name}_Square", amplitude_scale=cr_cancel_amp_scaling)
        # align for the next step and clear the phase shift
        align(*elems)
        reset_frame(cr.name)
        reset_frame(qt.xy.name)

    elif cr_type == "direct+cancel+echo":
        # phase shift for cr drive
        cr.frame_rotation_2pi(cr_drive_phase)
        qt.xy.frame_rotation_2pi(cr_cancel_phase)
        # direct + cancel
        align(*elems)
        cr.play("square", amplitude_scale=cr_drive_amp_scaling)
        qt.xy.play(f"{cr.name}_Square", amplitude_scale=cr_cancel_amp_scaling)
        # pi pulse on control
        align(*elems)
        qc.xy.play("x180")
        # echoed direct + cancel
        align(*elems)
        cr.play("square", amplitude_scale=-cr_drive_amp_scaling)
        qt.xy.play(f"{cr.name}_Square", amplitude_scale=-cr_cancel_amp_scaling)
        # pi pulse on control
        align(*elems)
        qc.xy.play("x180")
        # align for the next step and clear the phase shift
        align(*elems)
        reset_frame(cr.name)
        reset_frame(qt.xy.name)