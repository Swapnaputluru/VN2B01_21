tuple1 = ()
print("Nothing added to tuple:", tuple1)
tuple1 = (2)
print("one value added to tuple:", tuple1)
tuple1 = (2, 3, 4, 5)
print("few values added to tuple:", tuple1)
# indexing
tuple2 = ("swapna", "hanu", "anu", "diviyansh")
print("get the value by using index:", tuple1[3])
print("get the string by using index:", tuple2[2])

# slicing
print("get the values by using slicing:", tuple1[:2])
print("get the strings by using slicing:", tuple2[2:3])
print("get the strings by using slicing:", tuple2[0:])

tup1 = (1, 2, 3, 4)
tup2 = ("apple", "mango", "grapes", "banana")
print("concatenate 2 tuples", tup1 + tup2)
print("concatenate 2 tuples", tup2 + tup1)
print("Multiplying  tuple", tup2 * 2)
print("find the length:", len(tup1))
print("max value:", max(tup1))
print("min value:", min(tup2))
print("min value:", min(tup2))
# conversion of list to tuple
num = [3, 454, 67, 85, 456, 354, 65]
print(num, type(num))
num = tuple(num)
print(num, type(num))

# use the list function to list with in the tuple
tuple3 = ("hi","hello", ["welcome", "thankyou"])
tuple3[2].append("note")
print(tuple3)
tuple3[2].pop(1)
print(tuple3)

# loops tuple
tup1 = ("apple", "banana", "cherry")
for i in tup1:
  print(i)
for i in range(len(tup1)):
  print(i, ":", tup1[i])








