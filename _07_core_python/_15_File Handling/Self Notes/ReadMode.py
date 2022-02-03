print("--------------- open------------------")
file = open("file.txt", "r")
print(file.read())
file.close()

print("---------------with open------------------")
with open("file.txt") as f:
    print(f.read())

print("---------------by using loop------------------")
f2 = open("file.txt", "r")
for i in f2:
    print(i, end="")
f2.close()


print("---------------by using readline------------------")
file1 = open("file1.txt", "r")
print(file1.readline(), end="")
print(file1.readline())
file1.close()

print("---------------by using readlines------------------")
file1 = open("file1.txt", "r")
print(file1.readlines())
file1.close()
print("---------------by using read with characters------------------")
file1 = open("file1.txt", "r")
print(file1.read(5))
print(file1.read(10))
print(file1.readline(15))
file1.close()
print("---------------from another directory------------------")
interview = open(r"C:\Users\PUTLURU SWAPNA\Desktop\VN2B01_TRAINING\_07_core_python\_10_OPPs concepts\Self notes\notes on opps.txt", "r")
print(interview.read())
interview.close()
print("---------------r+ mode------------------")
n1 = open("read and write.txt", "r+")
n1.write("this is read and write mode")
print(n1.read())
n1.close()


