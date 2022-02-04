
print("----------simple pickling and unpickling------------")
import pickle
wishes = "# Happy Birthday My Dear!!!!"
file1 = open("test.txt", "wb")
pickle.dump(wishes, file1)
file1.close()
obj = open("test.txt", "rb")
print(pickle.load(obj))
obj.close()




