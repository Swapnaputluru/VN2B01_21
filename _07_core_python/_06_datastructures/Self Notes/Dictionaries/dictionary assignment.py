
print("--------convert 2 lists into dictionary---------")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = dict(zip(keys, values))
print(dict)

print("-------- Merge two Python dictionaries into one---------")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

print("-------- Print the value of key ‘history’ from the below dict---------")
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print("value of key ‘history’:", sampleDict["class"]["student"]["marks"]["history"])

print("-------- Initialize dictionary with default values---------")
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
emp1 = dict.fromkeys(employees,defaults)
print(emp1)
emp = {
    "kelly":{"designation": 'Developer',
             "salary": 8000},
    "emma":{"designation": 'Developer',
            "salary": 8000}
}
print(emp)

print("-------- Delete a list of keys from a dictionary---------")
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)

print("-------- Check if a value exists in a dictionary---------")
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 100 in sample_dict.values():
    print("yes,given value present in sample_dict")
else:
    print("no")

print("-------- Rename key of a dictionary city to location---------")
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict.pop("city")
sample_dict.setdefault("location", "new york")
print(sample_dict)

dict1 = {'Gfg': 4, 'is': 5, 'best': 9}
dict2 = [8, 3, 2]



