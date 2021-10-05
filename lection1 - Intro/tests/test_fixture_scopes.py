import pytest
import random


@pytest.fixture(scope="function")
def function_fixture():
    return random.randint(0, 100)


@pytest.fixture(scope="class")
def class_fixture():
    return random.randint(0, 100)


@pytest.fixture(scope="session")
def session_fixture():
    return random.randint(0, 100)


# def test_fixture_one(function_fixture, session_fixture):
#     print("func fixt %i", function_fixture)
#     print("sess fixt %i", session_fixture)
#     assert False
#
#
# def test_fixture_two(function_fixture, session_fixture):
#     print("func fixt %i", function_fixture)
#     print("sess fixt %i", session_fixture)
#     assert False


class TestFixtureOne:
    def test_fixture_one(self, function_fixture, class_fixture):
        print(f"clas fxt {class_fixture}, func fixt {function_fixture}")
        assert False

    def test_fixture_two(self, function_fixture, class_fixture):
        print(f"clas fxt {class_fixture}, func fixt {function_fixture}")
        assert False


class TestFixtureTwo:
    def test_fixture_one(self, function_fixture, class_fixture):
        print(f"clas fxt {class_fixture}, func fixt {function_fixture}")
        assert False

    def test_fixture_two(self, function_fixture, class_fixture):
        print(f"clas fxt {class_fixture}, func fixt {function_fixture}")
        assert False
