'''
 raise the exception and text by user
x = 10

if x < 11:
  raise Exception("Sorry, no numbers below 11")
'''

name = input("Enter the name:")
try:
    print(name + 10)
except:
    raise Exception("Concatenate error")

finally:
    print("program ended")
