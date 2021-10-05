import random


class Random:

    def __enter__(self):
        print("entering random")
        return random.randint(0, 100)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting radnom")


with Random() as r:
    print(r)
    print("inside 1")  # 48


with Random() as r:
    print(r)
    print("inside 2")


