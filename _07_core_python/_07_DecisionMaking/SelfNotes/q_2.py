
'''
Q.2.  Accept the percentage from the user and display the grade according to the following criteria:
Below25-----D
25 to 45----C
45 to 50----B
50 to 60----B+
60 to 80----A
Above 80----A+
'''

percentage = float(input("Enter the percentage:"))
if 0 <= percentage <= 100:
    if percentage < 25:
        print("your grade is D")
    elif 25 <= percentage < 45:
        print("your grade is C")
    elif 45 <= percentage < 50 :
        print("your grade is B")
    elif 50 <= percentage < 60:
        print("your grade is B+")
    elif 60<= percentage < 80:
        print("your grade is A")
    else:
        print("your grade is A+")
else:
    print("Out of percentage range")
