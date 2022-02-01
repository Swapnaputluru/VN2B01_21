
age = int(input('Enter the age:'))
if 0 < age <= 110:
    print("Age is with in the limit")
    if 0 < age <= 1:
        print("Your stage of life is Infant")
    elif 2 <= age <= 4:
        print("Your stage of life is Toddler")
    elif 5 <= age <= 12:
        print("Your stage of life is Child")
    elif 13 <= age <= 19:
        print("Your stage of life is Teen")
    elif 20 <= age <= 39:
        print("Your stage of life is Adult")
    elif 40 <= age <= 59:
        print("Your stage of life is Middle age adult")
    else:
        print("Your stage of life is Senior adult")
else:
    print("Age is not with in the limit")

