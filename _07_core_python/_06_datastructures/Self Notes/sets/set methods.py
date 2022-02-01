set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {3, 5, 7, 2, 56, 3, 7, 8, 23}
print(set1)
print(set2)
print("---------add----------")
set1.add("swapna")
print("after adding swapna:", set1)


print("---------copy----------")
set3 = set1.copy()
print("copy from another set", set3)

# it creates new set by which are not present in set2
print("---------difference()----------")
set1 = set1.difference(set2)
print(set1)
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {3, 5, 7, 2, 56, 3, 7, 8, 23}
set2 = set2.difference(set1)
print(set2)

# it removes the same elements present in both sets
print("---------difference_update()----------")
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {3, 5, 7, 2, 56, 3, 7, 8, 23}
set2.difference_update(set1)
print(set2)


# it prints new set by which are not present in set2
print("---------intersection()----------")
set1 = set1.difference(set2)
print(set1)
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {3, 5, 7, 2, 56, 3, 7, 8, 23}
set2 = set2.intersection(set1)
print(set2)

# it prints the same elements present in both sets with in the given set
print("---------intersection_update()----------")
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {3, 5, 7, 2, 56, 3, 7, 8, 23}
set2.intersection_update(set1)
print(set2)

# if set1 elements and set2 elements are same(one element same also) it returns False
print("---------isdisjoint()----------")
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {3, 5, 7, 2, 56, 3, 7, 8, 23}
set2 = set2.isdisjoint(set1)
print(set2)


# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
print("---------isdisjoint()----------")
set1 = {"hi", "hello", "welcome"}
set2 = {3, 5, 7, 2, 56, 3, 7, 8, 23}
set2 = set2.isdisjoint(set1)
print(set2)

# The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
print("---------issubset()----------")
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6, 6, 7}
set1 = set1.issubset(set2)
print("set1 elements present in set2:", set1)


set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6, 6, 7}
set2 = set2.issubset(set1)
print("set2 elements present in set1:", set2)

print("---------issuperset()----------")
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6, 6, 7}
set1 = set1.issuperset(set2)
print("set1 elements present in set2:", set1)


set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6, 6, 7}
set2 = set2.issuperset(set1)
print("set2 elements present in set1:", set2)

# after using of frozenset function we can't add or remove the elements
set1 = {1, 2, 3, 4}
set = frozenset(set1)
print(set)
set.add(2)






















