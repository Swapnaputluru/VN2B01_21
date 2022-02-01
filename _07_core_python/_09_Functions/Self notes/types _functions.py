'''
1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type

'''

print("-------------with parameter and return type--------------------")
# we have to give print when we call the function , when we write return type in function


def names(name1, name2):
    return name1, name2


print(names("swapna", "sunny"))
print(names("iphone", "samsung"))


print("-------------with parameter and no return type--------------------")
# no need to give print when we call the function, because already we gave in function


def compliment(a, b):
    print("compliments are:", a, b)


compliment("looking beautiful", "and Pretty")

print("-------------without parameter and with return type--------------------")
# we have to give print when we call the function , when we write return type in function


def request():
    result = "please" + " allow me"
    return result


res = request()
print("The request is:", res)


print("-------------without parameter and return type--------------------")
# no need to give print when we call the function, because already we gave in function


def warning():
    print("The warning is: Don't go there")


warning()



