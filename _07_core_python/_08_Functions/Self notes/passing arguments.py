# Passing Arguments
'''
1. Positional arguments (Required arguments)
2. Default arguments
3. Keyword arguments (Named arguments)
'''

print("-------------Positional Arguments------------")
# no.of parameters should be equal to no.of arguments.otherwise it will give error


def fruits(f1, f2, f3):
    print(f1, f2, f3)


fruits("apple,", "orange,", "guava")


print("-------------Default Arguments------------")
# if p3 is taken default value 5, if we assign another to p3 , 5 will replace with new number


def prime_numbers(p1, p2, p3 = 5):
    print(p1, p2, p3)


prime_numbers("for p3 default value will print", 2, 3,)
prime_numbers("default value replace with new value 2" , 3, 7)


def even_numbers(e1, e2 = 2, e3 = 4):
    print(e1, e2, e3)


even_numbers("for e2,e3 default value will print", 2, 4, )
even_numbers("default value replace with new value 14", 16, 18)


def odd_numbers(o1 = 3, o2 = 7, o3 = 9):
    print(o1, o2, o3)


odd_numbers("default value replace with new value 13", 17, 21)


print("-------------Keyword Arguments------------")
# no need to follow the sequence i,e.l1,l2,l3,l4 . we will add values by using parameters keyword


def laptops(l1,l2,l3,l4):
    print("all laptops are:", laptops)


laptops("dell", "hp", "apple", "lenova")   # positioning arguments
laptops(l3 = "lenova", l1 = "hp", l4 =  "apple", l2 = "lenova")  # keyword arguments

