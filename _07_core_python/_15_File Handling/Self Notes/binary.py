binary = open(r"C:\Users\PUTLURU SWAPNA\Desktop\VN2B01_TRAINING\_02_HTML\self_notes\html-07 gallary\nature9.jpeg", "rb")
pic = open("naturepic.JPG", "wb")
for i in binary:
    pic.write(i)

