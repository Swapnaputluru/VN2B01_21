
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("Invalid input")
else:
    print(c)
