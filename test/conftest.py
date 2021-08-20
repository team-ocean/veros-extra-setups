import os


def pytest_addoption(parser):
    parser.addoption("--backend", choices=["numpy", "jax"], default="numpy", help="Numerical backend to test")


def pytest_configure(config):
    backend = config.getoption("--backend")
    os.environ["VEROS_BACKEND"] = backend
