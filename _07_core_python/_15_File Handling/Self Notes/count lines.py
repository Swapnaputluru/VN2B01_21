print("---------------------Count of lines-------------------------------")
def count():
    file = open("AppenMode.py")
    count = 0
    for i in file:
        count = count+1
    file.close()
    print("count of lines", count)


count()


print("---------------------Count of lines which is starts with a-------------------------------")
L = ["apple \n", "sony \n", "lock \n", "alone \n", "Depression \n", "like \n", "Affection\n", "laxmi \n","allow \n"]
def count1():
    file = open("text.txt", "r+")
    file.writelines(L)
    count = 0
    for i in file:
        if i[0] in "a":
            count = count+1
    file.close()
    print("count of lines with 'a'::", count)


count1()


def count_letter():
    file = open("text.txt", "r+")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count += 1
    print("Capital letters in text file", count)
    file.close()


count_letter()


def count_words():
    file = open("text.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word[-1] == 'e':
            count+=1
    print("last letter ends with 'e' in text file", count)
    file.close()

count_words()

