img1 = open(r"C:\Users\PUTLURU SWAPNA\Desktop\VN2B01_TRAINING\_02_HTML\self_notes\html-07 gallary\swapna.jpg", "rb")
img2 = open("Swapna.jpg", "wb")
img = img1.read()
img2.write(img)
img1.close()
img2.close()

