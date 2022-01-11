student_details = {"name":"swapna",
                   "id": 143,
                   "clg_name":"K.S.R.M",
                    "address": {"district": "kadapa", "state": "andhra pradesh"}}
print("items of student details", student_details.items())
print("keys of student details", student_details.keys())
print("values of student details", student_details.values())
print("length of dictionary:", len(student_details))
print("nested value of address:", student_details["address"]["state"])
# add new key:value to dictionary
print("-------------------After adding new value-------------------")
student_details["mobile_no"] = 7142327531
print("items of student details after adding new value", student_details.items())
print("keys of student details after adding new value", student_details.keys())
print("values of student details after adding new value", student_details.values())
print("length of dictionary after adding new value:", len(student_details))


print("-------------------change items----------------------")
student_details["name"]="padma"
print(student_details)
student_details.update({"name":"hanu"})
print(student_details)

grade1 = {
    "A1": "91-100",
    "A2": "81-90",
    "B1": "71-80",
    "B2": "61-70"
}

grade2 = {
    "C1": "51-60",
    "C2": "41-50",
    "D1": "33-40"
}
print("grade1:", grade1)
print("grade2:", grade2)
grade1.update(grade2)
print("after update:", grade1)

for keys,values in grade1.items():
    print(keys, ":", values)



