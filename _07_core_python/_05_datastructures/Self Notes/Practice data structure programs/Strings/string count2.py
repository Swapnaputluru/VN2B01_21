
# builtin function
sentence = input("Enter sentence:")
print("Count of 'e'", sentence.count("e"))
print("Count of 'a'", sentence.count("a"))
print("Count of 's'", sentence.count("e"))

# by using algorithm
fruit = "watermelon"
c = 0
for i in fruit:
    if c == "e":
        c += 1
print("count of 'e' :", fruit.count("e"))

# by using function
sentence = input("Enter sentence:")


def find(name):
    return name.count()


print("Count of 'e':", sentence.count("e"))
print("Count of 'a':", sentence.count("a"))