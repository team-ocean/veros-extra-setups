import pytest


@pytest.fixture(autouse=True)
def ensure_diskless():
    from veros import runtime_settings

    object.__setattr__(runtime_settings, "diskless_mode", True)


def test_setup_acc_sector():
    from veros_extra_setups.setups.acc_sector import ACCSectorSetup

    sim = ACCSectorSetup()
    sim.setup()

    with sim.state.settings.unlock():
        sim.state.settings.runlen = sim.state.settings.dt_tracer * 20

    sim.run()


def test_setup_fjord():
    from veros_extra_setups.setups.fjord import FjordSetup

    sim = FjordSetup()
    sim.setup()

    with sim.state.settings.unlock():
        sim.state.settings.runlen = sim.state.settings.dt_tracer * 20

    sim.run()


def test_setup_wave_propagation():
    from veros_extra_setups.setups.wave_propagation import WavePropagationSetup

    sim = WavePropagationSetup(override=dict(nx=100, ny=100, nz=50))
    sim.setup()

    with sim.state.settings.unlock():
        sim.state.settings.runlen = sim.state.settings.dt_tracer

    sim.run()
