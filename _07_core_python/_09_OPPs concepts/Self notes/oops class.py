1
print("-----------with using method and not init function-------------")


class sub:
    def subs(a,b):
        print(a-b)


sub.subs(10,5)
print("-----------with using init function not method-------------")


class Multiply:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(a*b)


number = Multiply(10,10)



print("-----------with using init function and method--------------")


class Mobiles:
    def __init__(self, mobile_name, cost):  # self is parameter, mobile_name,age are arguments
        self.mobile_name = mobile_name   # self.mobile_name, self.cost are instance variables
        self.cost = cost   # mobile_name, cost are local variables

    def show(self):  # this is method
        print(self.mobile_name, self.cost)


m1 = Mobiles("iphone", 50000)  # these are objects
m2 = Mobiles("samsung", 20000)
m3 = Mobiles("1+", 30000)

Mobiles.show(m1)  # calling
Mobiles.show(m3)
print("------------")
m2.show()
m3.show()


class Addition:
    def __init__(number, num1,num2):
        number.num1 = num1
        number.num2 = num2

    def add(number):
        num = number.num1 + number.num2
        print("addition of num1 and num2 is:", num)


n1 = Addition(12, 2)
Addition.add(n1)

class age:
    def __init__(self, age):
        self.age = age

    def select(self):
        if self.age <18:
            print("not eligible for vote and pension")
        elif 18 <= self.age <60:
            print("eligible for vote only not for pension")
        else:
            print("eligible for vote and pension")


a1 = age(int(input("Enter age:")))
a1.select()







'''

class Number:
 pass

n1 = Number()
print(n1)


class age:
    def __init__(self, list):
        self.list = list

    def select(self,list):
        for i in list:
            print("Okay")



a1 = list([1,2,4,6,77,45])


'''

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity

class Bus(Vehicle):
    print("This is bus")

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())