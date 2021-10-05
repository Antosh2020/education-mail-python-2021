def deco(f):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return f(*args, **kwargs)
    return wrapper


@deco
def my_sum(a: int, b: int):
    return a + b

print(my_sum(1, 2))

