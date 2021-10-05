import pytest
import random


@pytest.fixture(autouse=True,)
def new_file(random_file):
    f = open(random_file, 'w')
    f.write("fixture called")

    yield

    f.close()


@pytest.fixture()
def random_file():
    return str(random.randint(0, 100))


def test_autouse_fixture():
    assert True
