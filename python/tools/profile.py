import functools
import time
from contextlib import contextmanager


def function(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{func.__name__}: {result} ({t2-t1:.5f} seconds)")
        return result

    return wrapped


@contextmanager
def context(description: str = "statement"):
    t1 = time.perf_counter()
    yield  # do the stuff inside the with statement
    t2 = time.perf_counter()
    print(f"{description} took {t2-t1:.5f}s")
