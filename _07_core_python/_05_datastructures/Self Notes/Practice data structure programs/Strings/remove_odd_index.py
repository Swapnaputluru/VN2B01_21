# using built in

# using algorithm
word = input("enter the word:")
even = []
odd = []
for i in range(len(word)):
    if i % 2 == 0:
        even.append(word[i])
    else:
       odd.append(word[i])

print("even characters", format(even))
print("odd characters", format(odd))

# using function


def odd_values(line):
    result = " "
    for i in range(len(line)):
        if i % 2 == 0:
            result = result + line[i]
    print(result)


odd_values("swapnareddy")

