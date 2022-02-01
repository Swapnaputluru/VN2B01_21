'''
Errors are 3 types
1.Compile time Errors --- syntax error, wrong spelling,getting error while writing the code
1.Logical time Errors --- no issue in input and output will come,but output is wrong
3.Run time Errors --- divide by 0,name error like this

The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

print("exception handling while function calling")
def func(a):
    d = a % 0
    print(d)


try:
    func(3)
except:
    print("something wrong")
finally:
    print("End program")
print("----------------------------------------")
print("exception handling with in the function")

def function(a):
    try:
        d = a % 0
        print(d)
    except ZeroDivisionError:
        print("zero divisible error")
    finally:
        print("program ended")

function(12)
print("----------------------------")


def func(a, b):
    d = a % b
    print(d)


try:
    func(3, 0)
except ZeroDivisionError:
    print("Zero division error occurred")
else:
    print("Error occurred")
finally:
    print("End program")
print("------------------------")



