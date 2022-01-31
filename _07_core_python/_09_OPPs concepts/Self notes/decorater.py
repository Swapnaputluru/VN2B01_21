def divition(a, b):
    d= a / b
    print(d)
def smart_divition(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


div = smart_divition(divition)
div(10, 20)

div(20, 10)
div(4, 20)