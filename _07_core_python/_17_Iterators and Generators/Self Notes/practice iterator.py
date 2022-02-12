list1 = [2, 4, 44, 6, 7, 8]
print("<<<<<<<<<<<<<<< By using loop >>>>>>>>>>>>>>>>")
for i in list1:
    print(i)

print("<<<<<<<<<<<<<<< By using iterator >>>>>>>>>>>>>>>>")

iterator = iter(list1)
print(iterator.__next__())
print(next(iterator))
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()

print("<<<<<<<<<<<<<<< By using class>>>>>>>>>>>>>>>>")


class Iterator:
    def __init__(self):
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 10:
            val = self.number
            self.number += 1

            return val

        else:
            raise StopIteration


values = Iterator()
print(next(values))

for i in values:
    print(i)








