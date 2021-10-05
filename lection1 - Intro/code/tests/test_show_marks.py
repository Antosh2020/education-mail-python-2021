import pytest


@pytest.mark.smoke
def test_mark1():
    assert True


@pytest.mark.smoke
def test_mark2():
    assert True


@pytest.mark.regress
def test_mark3():
    assert True


class TestKeywordClass:
    def test_something(self):
        assert True

    def test_method_simple(self):
        assert True
