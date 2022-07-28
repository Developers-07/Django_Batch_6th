from StudentImplement import StudentImplement
from accounts import Accounts

std1 = StudentImplement("Zishan","CSE")
std2 = StudentImplement("Razib","CSE")
std3 = StudentImplement("Abir","EEE")

print(std1)
print(std2)
print(std3)

acc = Accounts("","")
acc.set_stu_name("Faruk")
acc.set_stu_dept("CSE")
print(acc.get_stu_name())
print(acc.get_stu_dept())