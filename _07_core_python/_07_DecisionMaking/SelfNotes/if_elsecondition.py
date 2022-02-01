


# if-else statement--1
number =  int(input("Enter number:" ))
if number%2 ==0:
    print('Even number')
else:
    print('Odd number')

print("--------------------------")

# if-else statement--2
name = input('enter name:' )
if name in ['swapna','hanu','padma','hema','laxmi'] :
    print('Yes, the name in the list')
else:
    print('No, the name not in the list')

# if-else statement--3
year = int(input("Enter the year:" ))
if year%4 ==0:
    print('Leap Year')
else:
    print('Not Leap Year')


a =  int(input("Enter first number:" ))
b =  int(input("Enter second number:" ))
if a<b:
    print("%d is gretest number"%b)
else:
    print("%d is gretest number" %a)