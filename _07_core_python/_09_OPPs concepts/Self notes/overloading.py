# class and method are same but gives different outputs depends on the arguments

class Age:
    def eligability(self, age):
        if 0 < age < 18:
            print("not eligible for vote and pension", age)
        if 18 <= age < 60:
            print("eligible for vote only", age)
        else:
            print("eligible for vote and pension", age)


a1 = Age()
a1.eligability(12)
a1.eligability(18)
a1.eligability(32)
a1.eligability(62)



def adding(a, b):
    add = a + b
    print(add)

def adding(a, b, c):
    add = a + b + c
    print(add)


adding(1, 2, 3)


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

