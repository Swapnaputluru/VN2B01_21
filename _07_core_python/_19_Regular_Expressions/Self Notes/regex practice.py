import re
line = "This is the regular expression"
print("==================using search====================")
line1 = re.search("the", line)
print(line1)
print(line1.group())

print('Start Index:', line1.start())
print('End Index:', line1.end())

name = "SUNNY"
print(re.search(r'[^a-z]', name))
print(re.search(r'[^A-Z]', name))
print("Any charecters  only gives first occurrence")
line5 = "raani raaju roja rohit raamu"
print(re.search(r"r...u", line5))
print(re.search(r"raa..", line5))

line2 = "The range provides the flexibility to match a text with the help of a range pattern"
a = re.search("^The.*pattern$", line2)
if a:
    print("Yes")
else:
    print("No")

print(re.search(r'\bthe\b', "thecitythe"))
print(re.search(r'\bthe\b', "the city the"))






