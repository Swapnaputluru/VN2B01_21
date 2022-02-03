try:
    age = int(input("Please enter your age: "))
    print("your %d years old." % age)
except ValueError:
    print("Hey, it is not a number!")

print("--------------Index error-----------------")
list = [2, 54, 7]
try:
 print(list[4])
except IndexError:
 print("Indexing error")
finally:
    print("ended")


print("----------------key error------------------")
dist = {
    "name": "swapna",
    "age": 23,
    "Location": "Anantapuramu",
    (1, 2, 3): "tuple"
}
try:
    print(dist["na"])
except KeyError:
    print("Key is wrong")
except:
    print("something wrong")
finally:
    print("finally executed")

print("----------------Name error------------------")


def names(n):
    n = "sunny"
    return n
try:
    print(names(n))
except NameError:
    print("name error occurred")
finally:
    print("thank you")


list1 = ['swapna', True, 0, 14.3]
for entry in list1:
    a = int(entry)
    try:
        print("the entry is:", entry)
        r = 1 / int(entry)
    except ValueError:
        print("ValueError exception occurred")
    except ZeroDivisionError:
        print("ZeroDivisionError exception occurred")
    except:
        print("some error occurred")
    else:
        print(r)
    finally:
        print("End the program")