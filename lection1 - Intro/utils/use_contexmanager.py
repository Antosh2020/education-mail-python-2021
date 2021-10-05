import random
from contextlib import contextmanager


@contextmanager
def random_func():
    print("entering random")
    yield random.randint(0, 100)
    print("exiting random")


with random_func() as r:
    print(r)
    print("inside 1")


with random_func() as r:
    print(r)
    print("inside 2")
