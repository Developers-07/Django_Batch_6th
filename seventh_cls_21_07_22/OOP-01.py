# class, object

# create a class
class Student:
    # class properties--> attributes/variables, constructor, function

    # global variables or instance
    name=""
    dept=""
    uid=""

    # constructor
    def __init__(self,name,dept,uid):
        self.name=name
        self.dept=dept
        self.uid=uid

    def __str__(self):
        return self.name+" "+self.dept+" "+self.uid
# create an object
s1=Student("zishan","cse","11449")

# print the object values
print(s1.name,s1.dept,s1.uid)
# print(s1)

s2=Student("razib","cse","11649")
print(s2.name,s2.dept,s2.uid)
# print(s2)

s3=Student("faruk","cse","11737")
print(s3)
