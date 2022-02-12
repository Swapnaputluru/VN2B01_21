'''
Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept.
It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

'''

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(17)

