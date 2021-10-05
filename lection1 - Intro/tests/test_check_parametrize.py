import pytest


@pytest.mark.regress
def test_check_odd():
    for i in range(10):
        assert i % 2 == 0


def test_check_odd_better():
    errors = list()
    for i in range(10):
        try:
            assert i % 2 == 0
        except AssertionError:
            errors.append(f"{i} is even")

    assert not errors


@pytest.mark.parametrize("i", list(range(10)))
def test_check_odd_parametrize(i):
    assert i % 2 == 0


@pytest.fixture(scope="function", params=[1, 2, 3, 4, 5])
def param_fixture(request):
    if request.param <= 3:
        return request.param * 10
    return request.param


# @pytest.mark.smoke
def test_use_parametrized_fixture(param_fixture):
    print(param_fixture)
