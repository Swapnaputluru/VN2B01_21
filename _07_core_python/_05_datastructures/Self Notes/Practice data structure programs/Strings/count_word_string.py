line = input("Enter line:")
l1 = line.split()
print("Count of words in string by using builtin function:",len(l1))

count = 0
for i in l1:
    count +=1
print("Count of words in string:",count)


def word(sentence):
    count = 0
    for i in sentence:
        count += i
        print(count)







word("hgduyf hfhd hhf")

