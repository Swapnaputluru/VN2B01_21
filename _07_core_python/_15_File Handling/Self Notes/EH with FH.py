import io

print("-------------file handling with exception handling--------------")
print("------------- FileNotFoundError--------------")
try:
    file = open("f.txt", "r")
    print(file.read)
except FileNotFoundError:
    print("file is not found")
finally:
    print("end")

print("------------- FileExistsError--------------")
try:
    file1 = open("file1.txt", "x")
except FileNotFoundError:
    print("file is not found")
except FileExistsError:
    print("file already exist ")
finally:
    print("end")

print("------------- UnicodeDecodeError--------------")
try:
    binary = open(r"C:\Users\PUTLURU SWAPNA\Desktop\VN2B01_TRAINING\_02_HTML\self_notes\html-07 gallary\nature9.jpeg", "r")
    print(binary.read())
except FileNotFoundError:
    print("file is not found")
except FileExistsError:
    print("file already exist ")
except UnicodeDecodeError:
    print("UnicodeDecodeError ")
finally:
    print("end")

print("------------- io.UnsupportedOperation--------------")
try:
    file1 = open("file1.txt", "r")
    file1.write("hi")
    print(file1.read())

except FileNotFoundError:
    print("file is not found")
except FileExistsError:
    print("file already exist ")
except  io.UnsupportedOperation:
    print("Unsupported Operation ")
finally:
    print("end")