'''
Python Operators:
Operators are used to perform operations on variables and values.
Operators are special symbols in Python that carry out arithmetic or logical computation.
The value that the operator operates on is called the operand. Here, + is the operator that performs addition.
2 and 3 are the operands and 5 is the output of the operation.

'''
# Python Arithmetic Operators
x = 10
y = 2
print (x + y) # Add--output =12
print (x - y) # Subtract  output =8
print (x * y) # Multiplication output =20
print (x / y) # Division  output =5.0
print (x // y) # no reminder  output =5
print (x % y) # Modulus(only reminder)  output =0
print (x ** y) # 10 power 2  output =100

# Python Assignment Operators
a = b = c = d = e = f = g = 10
a += 4     # same as a + 4
print( a )
b -= 4        # same as b - 4
print( b )
c *= 4       # same as c * 4
print( c )
d /= 4      # same as d / 4
print( d )
e %= 4     # same as e % 4
print( e )
f **= 4    # same as f ** 4
print( f )
g //= 4    # same as g // 4
print( g )


# Python Comparison Operators
y = 10
z = 8
print(z == y)    # output false because y and z values are not same
print(z != y)
print(z < y)
print(z > y)
print(z <= y)
print(z >= y)
print("-----------------------")

# Python Logical Operators
n = 4
print( n < 3 and n > 7 )  # output false because 2 statements are wrong
print( n > 3 and n < 7 )  # output true because 2 statements are right
print( n > 3 or n > 7 )  # output true because one  statement is right
print( not(n > 3 and n < 7) )  # output false because we are using not so the result will be reverse



