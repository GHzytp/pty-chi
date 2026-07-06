# Copyright © 2025 UChicago Argonne, LLC All right reserved
# Full license accessible at https://github.com//AdvancedPhotonSource/pty-chi/blob/main/LICENSE

from typing import Optional, Type, Union
from dataclasses import field
from pydantic.dataclasses import dataclass


import ptychi.api.options.base as base
import ptychi.api.options.task as task_options
import ptychi.api.enums as enums
import ptychi.forward_models as fm


@dataclass
class AutodiffReconstructorOptions(base.ReconstructorOptions):
    loss_function: enums.LossFunctions = enums.LossFunctions.MSE_SQRT
    """
    The loss function.
    """

    forward_model_class: Union[enums.ForwardModels, Type["fm.ForwardModel"]] = enums.ForwardModels.base
    """
    The forward model class.
    """

    forward_model_params: Optional[dict] = None
    """
    The forward model parameters.
    """

    def get_reconstructor_type(self) -> enums.Reconstructors:
        return enums.Reconstructors.AD_GENERAL


@dataclass
class AutodiffOptions(task_options.PtychographyTaskOptions):
    reconstructor_options: AutodiffReconstructorOptions = field(
        default_factory=AutodiffReconstructorOptions
    )
