'''

'''
# if-elif-else statement---1
age = int(input("Enter age:"))
if age < 18:
    print('not eligible for vote and pension')
elif 18 <= age < 60:
    print('Eligible for vote only')
else:
    print('Eligible for vote and pension')


# if-elif-else statement---2
time = int(input("Enter the time:" ))
if 6 <= time <= 18:
    print('Day shift')
elif 18 <= time <= 24 or 1 <= time <= 5 :
    print('Night shift')
else:
    print('Time out of range')

# if-elif-else statement---3
num = 86785
if 0 <= num <= 9:
    print('Single digit number')
elif 10 <= num <= 99:
    print('Two digit number')
else:
    print('More than three digit number')


