sentence = "Python is high level programming language"
res = sentence.split()
for i in res:
    length = 0
    print(i, len(i))
print()


line1 = input("Enter line1:")
line2 = input("Enter line2:")

print(len(line1), len(line2))
if len(line1) <= len(line2):
    print("Line2 is largest string ",  len(line2))
else:
    print("Line1 is largest string ", len(line1))


def fun():
   pass