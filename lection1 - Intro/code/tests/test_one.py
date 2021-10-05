import pytest
import random
#
# def test_dict_get_non_existing_key():
#     my_d = {
#         "key1": 'val1',
#         "key2": "val2"
#     }
#     with pytest.raises(KeyError):
#         my_d["key3"]


@pytest.fixture()
def random_value():
    print("entering")
    yield random.randint(0, 100)
    print("exiting")


def test_random_fixture(random_value):
    assert random_value > 50
