# dec.py
from time import time

def timer(func):
    def f(*a, **kwargs):
        before = time()
        rv = func(*a, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv
    return f

@timer
def add(x, y=10):
    return x + y


# print ('add(20,30)', add(20, 30))
print('add("a" "b")', add("a", "b"))
