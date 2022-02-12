import re

print("==================using findall====================")
line3 = "A regular expression is a powerful tool for matching text, based on a pre-defined pattern."
print(re.findall(r"[Aa]", line3 ))

line4 = "The range provides the flexibility to match a text with the help of a range pattern"
print(re.findall(r"[Tt]he", line4 ))

print("==================Characters between the a and q====================")
x = re.findall("[a-q]", "I am from VN2 Solutions")
print(x)

print("==================find the names====================")
line5 = "raani raaju roja rohit raamu"
print(re.findall(r"r...u", line5))
print(re.findall(r"raa..", line5))

print("==================starts with ====================")
print(re.findall(r"^the", "the bangulore city"))
a = re.findall(r"^the", "bangulore city")
if a:
    print("Yes")
else:
    print("No")

print("==================ends with ====================")
print(re.findall(r"the$", "the bangulore city"))
a = re.findall(r"city$", "bangulore city")
if a:
    print("Yes")
else:
    print("No")

print("==================0 or more occurrences====================")
x = re.findall("s.*y", "sony sunny syamy saru" )
print(x)

x = re.findall("se.+n", "this season is winter")
print(x)

x = re.findall("se.?n", "this season is winter")
if x:
    print("Yes")
else:
    print("No")

x = re.findall("se.{3}n", "this season is winter")
print(x)

x = re.findall("is|or", "this or that")
print(x)
# check starts with The or not
line = "The regular expression"
x = re.findall("\AThe", line)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
print("============\b used to begging of word or ending of word============")
y = re.findall(r"\breg", line)
print(y)
if y:
  print("Yes, there is a match!")
else:
  print("No match")

z = re.findall(r"lar\b", line)
print(z)
if z:
  print("Yes, there is a match!")
else:
  print("No match")

print("============\b used to not begging of word or ending of word============")

x = re.findall(r"\Beg", line)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


print("==================\d used find the digits====================")
d = re.findall("\d", "My Laptop is 50000")
print(d)


print("==================\D do not print digits====================")
d = re.findall("\D", "My Laptop is 50000")
print(d)

print("==================\s white spaces====================")
s = re.findall("\s", "My Laptop is 50000")
print(s)

print("==================\s not print white spaces====================")
s = re.findall("\S", "My Laptop is 50000")
print(s)
# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character

print("==================\w return a-z and 0-9 and _ ====================")
txt = "Created class ith name my_class 12%$^&$"
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("==================\w return (a-z and 0-9 and _) except these ====================")
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The Wonderlaa is famous in bangulore"
#Check if the string ends with "Spain":
x = re.findall("lore\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")