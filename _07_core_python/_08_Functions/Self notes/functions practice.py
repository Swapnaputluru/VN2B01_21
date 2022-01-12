print("----------without parameter------------")


def wish():
    print("All the best")


wish()
print("----------with parameter------------")


def wishes_name(name): # name is parameter
    print("happy birthday my dear", name) # body of function


wishes_name("Friend") # friend is argument
wishes_name("Anju")
print("-----------one operation-------------")


def fun(num1, num2): # num1, num2 are parameters
    result = num1 * num2  # remaining is body of function
    print("multiplication of num1 and num2:", result)


fun(10, 3)  # these 3 are arguments
fun(21, 24)
fun(73, 322)
print("-----------more than one operation-------------")


def arithmatic(a, b):
    output = a + b, a - b, a * b, a / b
    print(output)


arithmatic(3, 2)
arithmatic(10, 5)


def add_sub_multiply_division(x, y):
    add = x + y
    sub = x - y
    multiply = x * y
    division = x / y
    print("add:", add, "sub:", sub, "multiply:", multiply, "division:", division)


add_sub_multiply_division(12,10)
add_sub_multiply_division(123,4)
print("-----------give return--------------")


def add_sub(a, b):
    add = a + b
    sub = add - (a - b)
    return add, sub


print(add_sub(12, 3))
print("add:sub", add_sub(12, 3))


print("-----------user input given by user --------------")


def sum(num1, num2):
    print("sum of num1 and num2:", num1 + num2)


sum(int(input("Enter num1:")), int(input("Enter num2:")))



