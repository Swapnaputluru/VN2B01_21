from datetime import date
my_birthday_date = date(1998,6,17)

print("My Birth date is:", my_birthday_date)

today = date.today()

print("Current date is:", today)
print("Current year is:", today.year)
print("Current month is:", today.month)
print("Current day is:", today.day)

Str = date.isoformat(today)
print("String format", type(Str), Str)

from datetime import datetime
'''
date_time = datetime.fromtimestamp(1765254214)
print(date_time)
'''
from datetime import time
user_time = time(22, 34, 45)

print("Enter time is:", user_time)


'''
user_time = time(25, 34, 45)
print("Enter time is:", user_time)
  user_time = time(25, 34, 45)
 ValueError: hour must be in 0..23
 
user_time = time('16', 34, 45)
print("Enter time is:", user_time)
  user_time = time('16', 34, 45)
TypeError: an integer is required (got type str)
'''

print("<<<<<<<<<<<<Single input>>>>>>>>>>>>>>>")

single_input = time(minute=45)
print(single_input)

print("<<<<<<<<<<<<No input>>>>>>>>>>>>>>>")
no_input = time()
print(no_input)
print("<<<<<<<<<<<< Output separately >>>>>>>>>>>>>>>")
given_time = time(12, 40, 56, 3)
print(given_time.hour)
print(given_time.minute)
print(given_time.second)
print(given_time.microsecond)

from datetime import timedelta
print("<<<<<<<<<<<< Current date and time >>>>>>>>>>>>>>>")
current_datetime = datetime.now()
print(" Current date and time ::", current_datetime)
print("<<<<<<<<<<<< After 2 days date and time >>>>>>>>>>>>>>>")
after_2days_datetime = current_datetime + timedelta(days = 2)

print(" After 2 days date and time ", after_2days_datetime)
print("<<<<<<<<<<<< Difference between date and time >>>>>>>>>>>>>>>")
print(after_2days_datetime- current_datetime)


print("<<<<<<<<<<<< Calendar >>>>>>>>>>>>>>>")
import calendar

a = calendar.month(2022,6)
print(a)

