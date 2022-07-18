
# def first_fun():
#     return "Good Night"
#
# def another_fun():
#     print("Good Morning")
#
# ans=first_fun()
# print(ans)
# another_fun()

dic = {
    "Name":"Zishan",
    "Age": 22
}

def my_get(key):
    for k, v in dic.items():
        if k == key:
            return dic[k]
    return "No Items"
ans=my_get("Age")
print(ans)
ans=my_get("address")
print(ans)

# def my_sum(a,b):
#     return a+b
#
# sum=my_sum(10,30)
# print(sum)