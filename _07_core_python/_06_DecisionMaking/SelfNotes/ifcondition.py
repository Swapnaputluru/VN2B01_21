
# data type integer and arthamatic operators and comaparision operators
x = 15
y = 10
print('addition of x and y:', x + y)   # output 25
print('subtraction of x and y:', x - y)   # output 5
print('multiplication of x and y:', x * y)   # output 150
print('modulus of x and y:', x % y)   # output 5
print('division of x and y:', x / y)   # output 1.5

# Addition and equals too, grater than comparison operator
if ( x + y == 25 ):   # when this statement is true, print is executed
    print("it's True")   # True
if ( x + y > 30):   # when this statement is false, print is notexecuted , goes to another statements
    print("x+y is grater than 30")  # False

# subtraction and less than comparison operator
if (x - y < 20):
    print("x-y is less than 20")   # True


# Multiplication and not equal to, grater than comparison operator
if (x * y != 25):
    print("x*y is not eual to 25")  # True
if (x * y >72275874):
    print("x*y is grater than 72275874")  # False

# Modulus and  equal to, grater than equal to comparison operator
if (x % y == 25):
    print("x%y is equals 25")   # False
if (x % y >= 2 ):
    print("x%y grater than or equals to 2 ")  # True

# division and  equal to, grater than equal to comparison operator
if (x / y >= 5):
    print("x/y is grater than 5")   # False
if (x / y == 1.5):
    print("x/y is equals 1.5") # True

# Datatype is integer and comparison operators used
marks = 34
if ( marks >= 35):
    print('pass') # False
if (marks<35):
    print('fail') # True


# Data type string and logical operators

name = "swapna"
age = 24

# And logical operator
print("-----------------and---------------")
if name=='swapna' and age == 24 :
    print('both conditions true') # True
if name=='swapna' and age > 24 :
    print('one condition true and another condition false') # False
if name=='hanu' and age != 24 :
    print('both conditions false') # False
print("-----------------or---------------")
# Or logical operator
if name == 'swapna' or age == 24 :
    print('both conditions true') # True
if name=='swapna' or age > 24 :
    print('one condition true and another condition false') # True
if name=='hanu' or age != 24 :
    print('both conditions false') # False


print("-----------------not---------------")
# Not logical operator
if name=='swapna' or age > 24 :
    print(not('one condition true and another condition false')) # True
if name=='hanu' or age != 24 :
    print(not('both conditions false'))# False
if True: print('condition is true')
if False: print('condition is false')
if name=='swapna' and age == 24 :
    print(not('both conditions true')) # True

print('------------------------------------')



a = 10
if a == 10: print("it's true")
if True:
    print('true')
if False:
    print('false')
if not False:
    print('ok')
if not None:
    print('not none')
if not 0:
    print('not zero')
if 0:
    print('zero')




