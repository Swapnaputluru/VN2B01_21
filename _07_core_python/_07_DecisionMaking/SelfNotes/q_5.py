'''
Q.5.Accept the number of days from the user and calculate the charge for library according to following:
Till 5 days : Rs 2/day
6 to 10 days : Rs 3/day
11 to 15 days : Rs 4/day
after 15 days : Rs 5/day
'''

number_of_days= int(input("Enter the number of days:"))
if number_of_days <= 5:
    charge =number_of_days *2
    print("Your charge is  :", charge)
elif 6 <= number_of_days <= 10:
    charge =number_of_days *3
    print("Your charge is :", charge)
elif 11 <= number_of_days <= 15:
    charge =number_of_days *4
    print("Your charge is :", charge)
else:
    charge =number_of_days *5
    print("Your charge is :", charge)


