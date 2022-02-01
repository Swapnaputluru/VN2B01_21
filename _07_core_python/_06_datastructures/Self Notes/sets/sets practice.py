set1 = {}
print(set1, type(set1))

set1 = {2}
print(set1, type(set1), len(set1))

set1 = {"swapna", True, 12.5, 642}
print(set1, type(set1))
num = set({12,45,567,True,"hi"})
print(num)
print("length of set:", len(num))
# Once a set is created, you cannot change its items, but you can remove items and add new items.
set2 = {123, 45, 67.67, "iphone", "mango"}
print(set2)
print("-------------adding --------------")
set2.add("samsung")
set2.add((1231,443,7,65,45))
print(set2)
print("-------------adding of 2 sets by using update--------------")
set1.update(set2)
print(set1)
print("-------------update--------------")
set2.update("hanu", "appo")
print(set2)

# To remove an item in a set, use the remove(), or the discard() method.
print("-------------remove item--------------")
names = {"swapna", "hanu", "paddu", "tom", "motu"}
print(names)
names.remove("swapna")
print("after removing swapna:", names)
names.discard("hanu")
print("after discard hanu:", names)
names.pop()
print("after using pop:", names)
names.clear()
print("after using clear:", names)
names = {"swapna", "hanu", "paddu", "tom", "motu"}
print(names)
'''
del names
print("after deleting", names)
'''

names = {"swapna", "hanu", "paddu", "tom", "motu"}
print(names)
for i in names:
    print(i)
print("--------------------------------")
name = ["swapna", "hanu", "paddu"]
for names in name:
    print(name)

print("--------------union------------------")
set1 = {1, 3, 56, 23, "hello", "hi", 45, 867, 756, 234}
set2 = {"hi", "hello", "welcome", 2022}
set1 = set1.union(set2)
print(set1)
print("--------------intersection------------------")
set1 = {1, 3, 56, 23, "hello", "hi", 45, 867, 756, 234}
set2 = {"hi", "hello", "welcome", 2022}
set3 = set1.intersection(set2)
print(set3)

# non-common elements in the both sets will be print
set1 = {1, 3, 56, 23, "hello", "hi", 45, 867, 756, 234}
set2 = {"hi", "hello", "welcome", 2022}
set3 = set1.symmetric_difference(set2)
print(set3)

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
set1 = {1, 3, 56, 23, "hello", "hi", 45, 867, 756, 234}
set2 = {"hi", "hello", "welcome", 2022}
set1.symmetric_difference_update(set2)
print(set1)

