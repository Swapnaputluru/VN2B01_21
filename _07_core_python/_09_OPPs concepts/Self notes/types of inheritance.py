print("------------------------simple and single inheritance-------------------------")
# single parent class and single child class
class parent:
    def mother(self):
        print("I am the mother ")
class child(parent):
    def daughter(self):
        print("I am the daughter ")
print("---------------calling parent")
p1 = parent()
p1.mother()
print("---------------calling child")
d1 = child()
d1.mother()
d1.daughter()
# method resolution Order
print(child.mro())
print("------------------------Multi level inheritance----------------------------")
# one super class ,one subclass and one sub subclass
class A:
    def addition(self, a, b):
        self.a = a
        self.b = b
        print("addition", a+b)


class B(A):
    def multiplication(self, a, b):
        self.a = a
        self.b = b
        print("multiplication", a*b)


class C(B):
    def subtraction(self, a, b):
        self.a = a
        self.b = b
        print("subtraction", a-b)
print("------------------addition")
a1 = A()
a1.addition(2,3)
print(A.mro())
print("------------------multiplication")
b1 = B()
b1.multiplication(2,4)
b1.addition(253,5634)
print(B.mro())
print("------------------subtraction")
c1= C()
c1.subtraction(6,3)
c1.addition(6,7)
c1.multiplication(2,43)
print(C.mro())


print("----------------------Hierarchical Inheritance------------------------")

# one superclass and 2 or more subclass

class Parents:
    def mother(self):
        print("i am the mother of this child")

    def father(self):
        print("i am the father of this child")

class Child1(Parents):
    def firstchild(self):
        print("i am the first child")


class Child2(Parents):
    def secondchild(self):
        print("i am the second child")


class Child3(Parents):
    def thirdchild(self):
        print("i am the third child")

print("------------------child1")
c1= Child1()
c1.mother()
c1.father()
c1.firstchild()
print(Child1.mro())
print("------------------child2")
c2= Child2()
c2.father()
c2.mother()
c2.secondchild()
print(Child2.mro())
print("------------------child3")
c3= Child3()
c3.father()
c3.mother()
c3.thirdchild()
print(Child3.mro())
print("---------------Multiple inheritance---------------------")

class Sunny:
    def __init__(self):
        print("print Sunny")


class Syam:
    def __init__(self):
        print("print Syam")

class Sony:
    def __init__(self):
        print("print Sony")


class NickNames(Sony,Sunny,Syam):
    def __init__(self):
        super().__init__()
        print("print Nick names")

s1 = NickNames()
print(NickNames.mro())

print("---------------------Hybrid inheritance--------------------")
# Multiple types of inheritance
# in this hierarchical, multi level inheritance used
class Mouse:
    def RightClick(self):
        print("mouse right click")

    def LeftClick(self):
        print("mouse left click")

class Mouse1(Mouse):
    def colour(self):
        print("black")


class Mouse2(Mouse):
    def brand(self):
        print("dell")


class Mouse3(Mouse1,Mouse2):
    def button(self):
        print("wheel")


print("-------------Mouse-----------------")
m1 = Mouse()
m1.LeftClick()
m1.RightClick()
print(Mouse.mro())
print("-------------Mouse1-----------------")
m2 = Mouse1()
m2.LeftClick()
m2.RightClick()
m2.colour()
print(Mouse1.mro())
print("-------------Mouse2-----------------")
m3 = Mouse2()
m3.LeftClick()
m3.RightClick()
m3.brand()
print(Mouse2.mro())
print("-------------Mouse3-----------------")
m4 = Mouse3()
m4.LeftClick()
m4.RightClick()
m4.colour()
m4.brand()
m4.button()
print(Mouse3.mro())




class cruelanimals:
    def animals(self):
        print("chirutha","lion","tiger","fox")


class seaanimals():
    def animals2(self):
        print("fish","amibha","penguin")

class totalanimals(seaanimals,cruelanimals):
    pass


c1 = totalanimals()
c1.animals()
c1.animals2()
