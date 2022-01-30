
from multipledispatch import dispatch

@dispatch(int, int)
def adding(a, b):
    add = a + b
    print(add)


@dispatch(int, int, int)
def adding(a, b, c):
    add = a + b + c
    print(add)


adding(1, 2)
adding(1, 2, 3)
