print("fibonacci sequence")
a = 0
b = 1
for i in range(10):

    print(a, end = ",")
    c = a + b
    a = b
    b = c
print()

print("display elements from a given list present at odd index positions")
list = [1, 5, 6, 7, 8, 8, 7, 5, 8, 8, 8, 6]
for i in list[1::2]:
    print(i, end=",")
print()
print("display elements from a given list present at even index positions")
for i in list[0::2]:
    print(i, end=",")

print("Calculate the cube of all numbers from 1 to a given number")
num =int(input("enter the number:"))
for i in range(1, num+1):
    print(i**3)


print("Find the sum of the series up to n terms")
num =int(input("enter the number:"))
start = 2
sum = 0
for i in range(1, num+1):
    print(start, end="+")
    sum += start
    start = start * 10 + 2
print("=", sum)

i = 1
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end = "")
    print()

for i in range(5,0,-1):
    for j in range(0, i):
        print(j, end="")
    print()