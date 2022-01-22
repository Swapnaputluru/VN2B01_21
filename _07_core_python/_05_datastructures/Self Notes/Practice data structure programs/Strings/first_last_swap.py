word = "Inheritance"
i1 = word[-1]
print(i1)
i2 = word[0]
print(i2)
print("Before swapping:", word)
print("After swapping:", i1 + word[1:10] + i2)

for i in word:
    if i == "I" or i == "e":
        continue
print(word.replace(word[0], word[-1])+ word.replace(word[-1], word[0]))


print()

def swap():

    pass







