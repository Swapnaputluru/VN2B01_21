print("Reverse a list in Python")
list1 = ['a', 'b', 'c', 'd']
list1.reverse()
print(list1)

print("Concatenate two lists")
list2 = ["I am", "from"]
list3 = ["swapna", "tadpatri"]
print(list2 + list3)

print("Turn every item of a list into its square")
list1 = [1, 2, 3, 4]
sqare = []
for i in list1:
    sqare.append(i ** 2)
print(sqare)

print(" Concatenate two lists")
list1 = ["hi", "are u"]
list2 = [" swapna", " paddu"]
for i in list1:
    for j in list2:
        print(i + j, end=",")
print()


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["h", "i", "j"])
print(list1)

