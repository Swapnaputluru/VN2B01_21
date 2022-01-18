list = [12, 42, 654, 7, 87, 88, 66, 67, 56, 34]
def list(list):
    for i in list:
        print(i, end=",")


list([12, 42, 654, 7, 87, 88, 66, 67, 56, 34])

print()


list([12,45,765,8,8])

print(" Create a function in Python")
def name_age(name,age):
    print(name, age)

name_age("swapna,", 23)
name_age("hanu,", 30)


print("Create a function with variable length of arguments")
def numbers(*nums):
    for i in nums:
        print(i)

numbers(12, 324, 54, 365, 87)
numbers(-3)

print("Return multiple values from a function")
def calculation(a, b):
    add = a+b
    sub = a-b
    return add,sub
print(calculation(23,20))


print("Create a function with default argument")
def show_salary(name,n1 = 9000):
    print(name,n1)
show_salary("akash")
show_salary("abhi", 10000)


print(" Create an inner function to calculate the addition")
def demo(a, b):
    def addition(a,b):
        add = a+b
        return add
    add = a+b
    return add + 5
print(demo(10,5))


print(" replace function name with new name")
def demo(a, b):
   print(a, b)

demo(10, 2)
sample = demo

sample(2, 3)




print("Generate a Python list of all the even numbers between 4 to 30")
list = []
for i in range(4,31,2):
     list.append(i)

print(list)


