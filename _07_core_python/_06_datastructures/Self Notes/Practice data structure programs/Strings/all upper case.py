print("(----------by using built in function--------------)")
change = "i am sunny from tadpatri"
u = change.upper()
print(u)

print("(----------by using algorithm--------------)")
for i in change:
    print(i.upper(), end="")
print()
print("(----------by using function--------------)")


def upper_case(sentance):
    print(sentance.upper())


upper_case(input("Enter sentance:"))

print()

print("(----------by using class--------------)")
class change_case:
    def __init__(self, s):
        self.s = s
        print(self.s.upper())


s = change_case("covert all lo")


