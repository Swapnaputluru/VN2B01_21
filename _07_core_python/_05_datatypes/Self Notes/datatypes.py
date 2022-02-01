'''
The following are Data types
integer(int-Numariacal values),
float(Decimal values)
bollean(bool-True or False)
sometimes string (any data type but within the collens)
'''
x = 20
print( x, type( x ) ,id( x ))
y = 10.5
print( y, type( y ) ,id( y ))
z = True
print( z, type( z ) ,id( z ))
w = 'swapna'
print( w, type( w ) ,id( w ))


#covert one datatype to another data type
# integer to float
a = 3
print( a, type( a ) ,id( a ))
a = float( a )
print( a, type( a ) ,id( a ))

#integer to boolean---all integers true except zero,only zero false
b = 57
print( b, type( b ) ,id( b ))
b = bool( b )
print( b, type( b ) ,id( b ))

#integer to string
c = 752
print( c, type( c ) ,id( c ))
c = str( c )
print( c, type( c ) ,id( c ))

#bool to integer
d = True
print( d, type( d ) ,id( d ))
d = int( d )
print( d, type( d ) ,id( d ))
# The output is 1,because we gaveue True and output is zero when we give false

#integer to complex
e = 8384
print( e, type( e ) ,id( e ))
e = complex( e )
print( e, type( e ) ,id( e ))

f = 2e4
print(f)

# Random number
import random
print(random.randrange(51,57))
