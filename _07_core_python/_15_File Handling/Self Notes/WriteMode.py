print("---------------only open------------------")
file = open("file.txt", "w")
file.write("hi sunny \n")
file.writelines("hello \n")
file.close()

print("---------------with open------------------")
with open("file.txt", "w") as file1:
    file1.write("Welcome to VN2 Solutions \n")

print("---------------another open------------------")
file = open("file1.txt", "w+")
print(file.read())
file.write("sample \n")
file.writelines("Text file \n")
file.close()

html = open("demo.html", "w+")
html.write("hello")
html.seek(0)
print(html.read())
html.close()
