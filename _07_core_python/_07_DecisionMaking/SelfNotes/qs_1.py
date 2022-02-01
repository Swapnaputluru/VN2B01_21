'''
Q.1. Accept the following from the user and calculate the percentage of class attended:
a.total number of working days
b.total number of days for absent
after calculating percentage show that, if the percentage is lessthan 75,than student will not be able to sit in exam
'''

workingdays = int(input("Enter working  days:"))
absent_days = int(input("Enter absent days:"))
present_days = workingdays - absent_days
result = present_days/workingdays
percentage = result * 100
print(percentage)
if percentage >= 75:
    print("Eligible for exams")
else:
    print("Not eligible for exams")