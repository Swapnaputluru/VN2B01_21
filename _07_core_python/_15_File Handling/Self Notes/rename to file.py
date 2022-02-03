import os
os.remove("html.html")
file = open("html.html", "r")
print(file.read())
# append and read mode