# Iterating string by using for loop (string assigning to variable)
name = "Swapna Reddy"
for x in name:
    print("Name character is:", x, type(x))

# Iterating string by using for loop  (string not assigning to variable)
for y in "Welcome To The Class":
    print(y, end=",")
print()
# by using end="," we will get output in one line only

# Iterating Tuple by using for loop
fruits = ('banana','apple','grapes', 'mango')
for a in fruits:
    print("The fruit name is:", a)

# Iterating list by using for loop  which is using by different datatypes
list = ['swapna', 12, 34.5, True, 'software']
for i in list:
    print("The value in list is: ", i, type(i))

# Iterating dictionary by using for loop
dictionary = {
    "name": "swapna",
    "marks": 87,
    "grade": "A+"
}
for a in dictionary.items():
    print(a)
for b in dictionary.keys():
    print("Only Keys:", b)
for c in dictionary.values():
    print("Only values:", c)

# Iterating adding 2 lists by using for loop
list1 = [1, 3, 5, 6, 8, 7, 8]
list2 = [4, 5, 7, 8, 8, 0]
for i in list1:
    for j in list2:
        print("Multiplication of list1 and list2:", i * j)

# Control Statements
# Break control statement
i = "Break control statement"
for j in i:
    print(j)
    j == c
    break






