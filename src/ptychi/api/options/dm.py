# Copyright © 2025 UChicago Argonne, LLC All right reserved
# Full license accessible at https://github.com//AdvancedPhotonSource/pty-chi/blob/main/LICENSE

from dataclasses import field
from pydantic import Field as PydanticField
from pydantic.dataclasses import dataclass

import ptychi.api.options.base as base
import ptychi.api.options.task as task_options
import ptychi.api.enums as enums


@dataclass
class DMReconstructorOptions(base.ReconstructorOptions):
    def get_reconstructor_type(self) -> enums.Reconstructors:
        return enums.Reconstructors.DM

    exit_wave_update_relaxation: float = PydanticField(default=1, ge=0, le=1)
    "Relaxation multiplier for the exit wave update."

    chunk_length: int = PydanticField(default=1, ge=1)
    """Number of scan points used in each chunk of the difference map exit wave update loop.
    Smaller values are more memory efficient, but can be slower."""


@dataclass
class DMObjectOptions(base.ObjectOptions):
    amplitude_clamp_limit: float = PydanticField(default=1000, gt=0)
    """Maximum allowed amplitude for the object reconstruction. Values above this will be clamped 
    to this value."""

    inertia: float = PydanticField(default=0, ge=0, le=1)
    "Inertia of the object update. Should be between 0 and 1."


@dataclass
class DMProbeOptions(base.ProbeOptions):
    inertia: float = PydanticField(default=0, ge=0, le=1)
    "Inertia of the probe update. Should be between 0 and 1."


@dataclass
class DMProbePositionOptions(base.ProbePositionOptions):
    pass


@dataclass
class DMOPRModeWeightsOptions(base.OPRModeWeightsOptions):
    pass


@dataclass
class DMOptions(task_options.PtychographyTaskOptions):
    reconstructor_options: DMReconstructorOptions = field(default_factory=DMReconstructorOptions)

    object_options: DMObjectOptions = field(default_factory=DMObjectOptions)

    probe_options: DMProbeOptions = field(default_factory=DMProbeOptions)

    probe_position_options: DMProbePositionOptions = field(default_factory=DMProbePositionOptions)

    opr_mode_weight_options: DMOPRModeWeightsOptions = field(
        default_factory=DMOPRModeWeightsOptions
    )
