
# Built in function approach
name = input("Enter name:")
print("Length of given name is:", len(name))

# Algorithm approach

employee_name = input("Enter the employee name: ")
count = 0
for name in employee_name:
    count += 1
print("length of the string by using algorithm approach", count)

# Using functions


def fruit(name_of_fruit= input("enter fruit name")):
    length = 0
    for i in name_of_fruit:
        length = length+1
    print(length)

fruit()

