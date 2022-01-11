from array import *

# 'i' is used to signed int i.e. both positive and negative numbers allows. otherwise it gives error
array1 = array("i", [1, -2, 4, -6, 8, 64])
print(array1, type(array1))

# 'I' is used to unsigned int i.e. only positive numbers allows. otherwise it gives error
array1 = array("I", [1, 2, 4, 6, 8, 64])
print(array1)

# 'd' is used to float values i.e. otherwise it gives error
array1 = array("d", [0.1, 42.54232, 12.4, 445.6, 65.8, 787.64])
print(array1)

# 'f' is used to float values with decimal values 16 i.e. otherwise it gives error
array1 = array("f", [0.877268581, 42.45435354232, 12.745734584, 445.7347576, 65.875758, 787.687545454])
print(array1)

# h for signed short int range -32768 to 32767
array2 = array("h", [121, -4245, 54, 7565, 6362, 5563, -32768, 32767])
print(array2)

# H for unsigned short int range 0 to 65,535
array2 = array("H", [12172, 42454, 54534, 7565, 63624, 55633, 32768, 32767, 0, 65535])
print(array2)

# l for signed long int range -2,147,483,648 to 2,147,483,647
array2 = array("l", [-767642712, 42454, 285872755, -2147483640, -754376362, -55633, 32768, 8586327, 0, 2147483640])
print(array2)

# L for unsigned long int range 0 to 4,294,967,295
array2 = array("L", [3485767642, 42454, 285872755, 58743775, 2754376362, 55633, 22232768, 238586327, 0, 287654655])
print(array2)

# b for unsigned char int range -128 to 127
array2 = array("b", [-128, 127, 0, -45, 45, -56, 34])
print(array2)

# B for unsigned char int range  0 to 255
array2 = array("B", [34, 255, 0, 54, 23, 56, 24, 65])
print(array2)
array2.pop(5)
print("after deleting index 5 value:", array2) # deleting value from specific index value
array2.insert(5, 65)
print("after inserting index 5 value:", array2)  # inserting value to specific index value
print("slicing from 0 to 6:", array2[0:6])  # slicing
print("count of 65 from array:", array2.count(65))  # count , how many times value occurs in array
array2.append(34)
print("added 34 to array at end by using append:"
      "", array2) # add value at end (append())
array2.extend((23, 55, 65)) # add values at end (extend())
print("added values to array at end by using extend:", array2)
array2.reverse()
print("array reverse", array2)