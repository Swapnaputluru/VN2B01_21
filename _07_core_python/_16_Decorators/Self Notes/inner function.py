import selenium


def factorial(n):
    def inner_factorial(n):
        if n == 0:
            return 1
        else:
            return n * inner_factorial(n-1)
    if type(n) == int and n >=0:
        return inner_factorial(n)
    else:
        raise TypeError("n should be a positve int or 0")


print("Factorial of 3:", factorial(3))
print("Factorial of 8:", factorial(8))


