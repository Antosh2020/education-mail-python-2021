import sys

import pytest
from _pytest.fixtures import SubRequest
import random


def is_master(config):
    if hasattr(config, "workerinput"):
        return False
    return True


@pytest.fixture(scope="session", autouse=True)
def check_us_worker_fixture(request: SubRequest):
    config = request.config
    sys.stderr.write(str(is_master(config)))


def pytest_configure(config):
    if is_master(config):
        print("!" * 10 + "This is configure hook from MASTER")
    else:
        sys.stderr.write("!" * 10 + f"This is configure hook from WORKER {config.workerinput['workerid']}\n")


def pytest_unconfigure(config):
    if is_master(config):
        print("!" * 10 + "This is unconfigure hook from MASTER")
    else:
        sys.stderr.write("!" * 10 + f"This is unconfigure hook from WORKER {config.workerinput['workerid']}\n")
