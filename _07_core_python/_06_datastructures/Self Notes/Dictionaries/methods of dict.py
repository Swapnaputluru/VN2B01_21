person = {
 "first.name": "swapna",
 "last.name": "reddy",
 "age": 24,
 "address": {"d.no": "12-4", "district": "Anantapuramu", "state": "Andhra pradesh"}
}
print(person)
print("-------------------get items----------------------")
print("last name:", person.get("last.name"))
print("address:", person.get("address"))
print("pincode:", person.get("pincode", 515408))
print(person)
print("-------------------dictionary items----------------------")
print(person.items())
print("-------------------dictionary keys----------------------")
print(person.keys())
print("-------------------dictionary values----------------------")
print(person.values())
print("-------------------pop() items----------------------")
person.pop("age")
print(person)
person.popitem()
print(person)

print("-------------------update items----------------------")
person.update({"age":24, "address" :{"d.no": "12-4", "district": "Anantapuramu", "state": "Andhra pradesh"}, "pincode": 515408})
print("person", person)

print("-------------------copy dictionary----------------------")
person2 = person.copy()
print("person2:", person2)

print("-------------------clear dictionary----------------------")
person2.clear()
print("person2:", person2)

print("-------------------fromkeys dictionary----------------------")
person = person.fromkeys(["swapna", "paddu", "hanu"], "welcome")
print("person:", person)

print("-------------------setdefault dictionary----------------------")
person.setdefault("diviyansh", "hi")
person.setdefault(12, [42.43,56,8565,78574])
print(person)

print("-------------------has key() dictionary----------------------")
print(person.has_key("paddu"))

