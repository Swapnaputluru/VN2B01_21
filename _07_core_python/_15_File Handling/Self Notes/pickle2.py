
print("------------by using list--------------------")
import pickle
my_list = ["sunny", 23, 3.43, True, "mango"]
list1 = open("list.txt", "wb")
pickle.dump(my_list, list1)
list1.close()
obj = open("list.txt", "rb")
print(pickle.load(obj))
obj.close()

print("------------by using function with dictionary--------------------")

def sample():
    dist1 = {
        "name" : "sunny",
        "age" : 20,
        "location" : "tadpatri"
    }

    dist2 = {
        "name": "sony",
        "age": 21,
        "location": "Bangalore"
    }

    dist3 = {
        "name": "sheeba",
        "age": 10,
        "location": "Anantapuramu"
    }
    dist4 = {
        "name": "manu",
        "age": 45,
        "location": "kundhanahalli"
    }
    all = dist1,dist2, dist3,dist4
    file1 = open("dictionary.txt", "wb")
    pickle.dump(all, file1)
    file1.close()
    obj = open("dictionary.txt", "rb")
    print(pickle.load(obj))
    obj.close()


sample()


