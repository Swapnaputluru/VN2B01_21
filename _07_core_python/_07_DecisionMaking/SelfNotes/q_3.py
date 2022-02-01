'''
Q.3. A company decided to give bonus to employee according to following criteria:
    Time period of service                        Bonus
     More than 10 years                            10%
     >=6 and <=10                                   8%
     Less than 6 years                              5%
  Ask user for their salary and years of service and print the net bonus amount.
'''

salary = float(input("Enter the Salary:"))
service_year = float(input("Enter the service_year:"))
if service_year > 10:
    bonus = salary * 0.10
    print("Bonus is 10% of salary:",bonus,"/net salary is:",bonus + salary)
elif 6 <= service_year <= 10:
    bonus = salary * 0.08
    print("Bonus is 8% of salary:",bonus,"/net salary is:",bonus + salary)
else:
    bonus = salary * 0.05
    print("Bonus is 5% of salary:", bonus, "/net salary is:", bonus + salary)

