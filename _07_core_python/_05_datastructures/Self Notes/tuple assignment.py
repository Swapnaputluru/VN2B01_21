print("Reverse the tuple")
tuple1 = (2, 3, 4, 5)
print(tuple1[::-1])


print("print 20 in the tuple")
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print("by using index:", tuple1[1][1])

tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)


print("Swap two tuples in Python")
tuple1 = (11, 22)
tuple2 = (99, 88)
print("before swapping of tuple1", tuple1)
print("before swapping of tuple2", tuple2)
tuple1, tuple2 = tuple2, tuple1
print("after swapping of tuple1", tuple1)
print("after swapping of tuple2", tuple2)


# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
print(tuple2)

# Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print("count of 50:", tuple1.count(50))

# Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 42)
for i in tuple1:
    if i == tuple1[0]:
        print(True, "=",i, end=",")
    else:
        print(False, "=",i)

