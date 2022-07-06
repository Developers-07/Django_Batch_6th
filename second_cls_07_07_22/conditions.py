a=int(input("Enter First Value "))
b=int(input("Enter Second Value "))

#type casting

#a=int(a)
#b=int(b)

if a>b:
    print("Condition is Correct")
else:
    print("Condition is Incorrect")

print("*"*50)

#nested condition

age=int(input("Enter your age = "))
if age>=18:
    nid=int(input("Enter your nid = "))
    if nid==1:
        print("You can give vote")
    elif nid==0:
        print("You can not give vote")
else:
    print("You are not able to give vote")

print("*"*50)

gpa=input("Enter your GPA ")
gpa=int(gpa)
if gpa>=33 and gpa<=100:
    print("pass")
else:
    print("fail")