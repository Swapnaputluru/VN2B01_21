'''
local variable is used only with in the function
global variable is used to anywhere in the program
when we have local and global variables it prefers local variable only

'''


print("-----using local & global variable-------")
name = "swapna"  # global variable
def names():
     name = "hanu"  # local variable
     print(name)
names()

# when we don't have local variable with in the function, globbal variable is come in output
print("-----global variable-------")
name = "swapna"  # global variable
def names():
     print(name)
names()

# when we use global keyword in the function that variable we can use anywhere in the program
print("-----local variable with global keyword-------")
def fruits():
     global fruit
     fruit = "guava"
     print(fruit)
fruits()

print(fruit)

print("-------------------------------------------------Lambda---------------------------------------------------------")
# performs in single line
x =lambda a, b, c,d:(a-b)+(c+d)
print(x(1, 3, 4, 6))
from functools import reduce
list1 = [5, 3, 56, 765, 454, 545, 65, 334, 52, 543, 56]

divisable_by_5 = list(filter(lambda i: i%5==0,list1))
addition = list(map(lambda a:a+3, divisable_by_5))
add = reduce(lambda a,b:a+b,divisable_by_5 )
print(divisable_by_5)
print(addition)
rint(add)







def cube(a):
     print(a*a*a)
lambda_cube = lambda a:a*a*a
cube(3)
print(lambda_cube(2))

