
'''
Lists are used to store multiple items in a single variable.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
'''
names = ['swapna', 'hanu', 'diviyansh', 'padma', 'hari', 'anu']
numbers = [18, 873, 80, 8, 38, 88]
print(names, type(names))
print(numbers, type(numbers))
# List items are indexed and you can access them by referring to the index number.The first item has index 0.
print(numbers[0])
print(names[4])
print(names[5])
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.
print(numbers[-3])
print(names[-2])
total = (names, numbers)
print(total)
numbers.append(8)
print(numbers)
numbers.remove(8)
print(numbers)
numbers.insert(3,55)
print(numbers)
numbers.pop()
print(numbers)
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
del names[2:]
print(names)
names.extend(['diviyansh','hari','anu'])
print(names)
print(min (numbers))
print(max (numbers))
print(sum (numbers))
numbers.sort()
print(numbers)
print(len(numbers))
print(len(names))
names = ['swapna', 'hanu', 'diviyansh', 'padma', 'hari', 'anu']
if 'swapna' in names:
    print("yes")
# To change the value of a specific item, refer to the index number.
names[2] = 'laxmi'
print(names)

