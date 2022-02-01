# by using builtin
company_name = "VN2 Solutions"
print(company_name[1:5])
print(company_name[:6])
print(company_name[0:])

# by using algorithm
for i in company_name:
    start = -1
    stop = 10
    start += 1
print(company_name[start:stop])

# by using functions
def display(vegetable, start, stop):
    print("Slicing of given vegetable:", vegetable[start:stop])


display("potato", 2, 6)
display("potato", 0, 6)
display("brinjal", 0, 4)
display("brinjal", 0, 7)