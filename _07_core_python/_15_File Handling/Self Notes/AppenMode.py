# print("---------------only open------------------")
file1 = open("file.txt", "a")
file1.write("Welcome to banglore city \n")
file1.close()
# print("---------------with open------------------")
with open("file.txt", "a") as file1:
    file1.write("Welcome to VN2 Solutions \n")

a = open("rename to file.py", "a+")
a.write("# append and read mode")
a.seek(0)
print(a.read())
a.close()
