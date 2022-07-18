# Dictionary(key-value pair)

dic={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4",
    "key5":"value5"
}
print(dic)
print(type(dic))

for i, j in dic.items():
    print(i,j)

print("*"*30)

# Nested dictionary

dic1={
    "Name":"Zishan",
    "Age":22,
    "Address":{
        "present":"Germany",
        "permanent":{
            "home1":"Satkhira",
            "home2":"Dhaka"
        }
    }
}
print(dic1)
print(dic1["Address"])
print(dic1["Address"]["permanent"])
print(dic1["Address"]["permanent"]["home1"])

dic1_update={"Name":"Disha"}
dic1.update(dic1_update)
print(dic1)

print("*"*30)

# list in dictionary

dic2={
    "Name": ["Alam","Monira","Zishan","Zihan"],
    "Dept": ["BBA", "IT", "CSE", "EEE"],
    "Sems": [12,10,8,6]
}
print(dic2)
for i,j in dic2.items():
    print(i,j[0])

print(dic2.values())
print(dic2.keys())
print(dic2.get("Sems"))
