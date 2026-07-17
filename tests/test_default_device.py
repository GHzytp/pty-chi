from types import SimpleNamespace

import torch

import ptychi.api as api
from ptychi.api.task import PtychographyTask


def test_gpu_default_device_falls_back_to_cpu_when_accelerator_unavailable(monkeypatch):
    previous_default_device = torch.get_default_device()
    torch.set_default_device("cpu")
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)

    task = PtychographyTask.__new__(PtychographyTask)
    task.reconstructor_options = SimpleNamespace(default_device=api.Devices.GPU)
    monkeypatch.setattr(task, "detect_launcher", lambda: None)

    try:
        task.build_default_device()

        assert torch.get_default_device().type == "cpu"
    finally:
        torch.set_default_device(previous_default_device)
