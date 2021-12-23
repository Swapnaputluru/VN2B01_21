#Notes about variables
#Variables are containers for storing values
x = 8
print( id(x), x)

'''
Here we given value 8 to the variable x
This is the write operation
in this 
x is variable,= is operater,8 is the value
print(x) is the read operation which gives results what we want like type of data,id of the value etc..
'''
print(type(x))
# get data type, here i got int because x value is integer
print(id(x))
# here i got id of value 8 is 431812575696...

print("_______________________________")
a = 10
b = 40
# here no need to mention data type, dynamically it will take.
c = a+b
print(c)
print(id(c), type(c))

d = 'swapna'
e = 10
f = 2.5
g = True  # first letter should be capital,otherwise it's not taken as boolean.
print(d, e, f, g)
print(id(d), type(d))
print(id(e), type(e))
print(id(f), type(f))
print(id(g), type(g))


_252 = 25
''' 
variable name does not start with numbers,in case we want with number start with under score(_).
special symbles also not allowed like @,&,* etc 
don't use upper case letters
'''
_1 = int(20.5)
_2 = float(10)
print(_1, _2)
'''
no need to mention data types
Here i mentioned datatype int and given value is float value i.e 20.5 ,
but when we given data type that value convert into what we given data type  so here i got value is just 20
same as for float given value is 10, but the output value is 10.0
'''
name = "swapna"
Name = 'swapna'
print(name, Name)
'''
Here python is case sensitive because given variable names are same just changed first letter i.e given capital letter
it is taken as two different variables
there is no change using single or double quotes , the output is same  
'''
'''
 Multi words variable names means variable names with more than one word
 camel case -- first word letter start with lower case letter and remaining words letters start with capital
 Ex:myCollegeName = "K.S.R.M"
 Pascal case-- Each word start with cappital letter
 Ex:MyCollegeName = "K.S.R.M"
 snake case--Each word separated by underscore
 Ex:my_college_name = "K.S.R.M"
'''
#Assign values
# multiple values to maltiple variables
a,b,c = 23,34,454
print(a,b,c)

#one value to multiple variables
x = y = z = "swapna"
print(x)
print(y)
print(z)

#Unpack a collection
names = ["swapna", "hanu", "diviyansh"]
s, h, d = names
print(h)
print(s)
print(d)

'''
If you combine two strings or two integers it will give output
If you try to combine a string and a number, Python will give you an error'''
a = "my name is "
b = "swapna"
print( a +  b )
c = 10
d = 20
print( c + d )
e = "swapna"
f = 2
print( e + f )
#  TypeError: can only concatenate str (not "int") to str




