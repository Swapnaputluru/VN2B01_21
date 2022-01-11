list1 = ["swapna", "hanu", "diviyansh", "yash", "paddu", "nilu"]
list2 = [34, 67, 76, 26, 78, 22, 56, 87, 66, 56, 88]
# append-----update
print("Before using append:", list1)
print("append use to add value to list ")
list1.append("laxmi")  # added string
list1.append({13.4, 576})
list1.append([2, 56, 7])  # added list# added set
print("After using append:", list1)
# extend
print("Before using extend:", list2)
print("extend use to add values to list ")
list2.extend(["sunny", "abhi", "balu"])  # string
list2.extend([234, 56, 75, {1:2, 2:4}])  # dictionary
print("After using extend:", list2)
# insert---is used to insert value in specific position
list3 = [24, 45, 87, 78, 23, 35, 54, 36, 53, 42]
print("Before using insert:", list3)
list3.insert(2, 2435)
list3.insert(2, "swapna")
list3.insert(4, ["name", "age"])
print("After using insert:", list3)

# pop-----delete by using index value
list4 = [234, 565, 7565, 57568, 5758, 46547, 285, 82457, 8745, 264]
print("Before using pop:", list4)
list4.pop()  # removes lase one
list4.pop(1)
print("After using pop:", list4)

# remove----delete value by using entering specific value
list4.remove(46547)
print("After using remove:", list4)

# count--count the number how many times occurs  in list
list5 = [23, 56, 788, 468, 867, 67, 78, 876, 67, 655, 76, 76, 23, 867, 468]
print("count the 67 occurs in list5:", list5.count(67))
print("count the 655 occurs in list5:", list5.count(655))

# index----it gives position of that number
print("it gives the position of number in list5:", list5.index(876))
print("it gives the position of number in list5:", list5.index(76))

# reverse---- it reverse the values
list6 = [5, 4, 3, 2, 1]
list6.reverse()
print("reverse values of list6:",list6)

# sort----it prints values ascending and descending orders
list7 = ["s","r","t","y","u","j","n","l","m"]
list7.sort()
print("it print string in ascending order:", list7)
list7.sort(reverse=True)
print("it print string in descending order:", list7)

# copy--- we will copy the whole list
num = [1, 5, 2, 7]
num1 = num.copy()
print("Original list:", num)
print("Copied list:", num1)
num.insert(2,4)
print("Insert a number to num and num1 won't take this number", num)
num.insert(1,10)
print("Insert a number to num1 and num won't take this number", num1)