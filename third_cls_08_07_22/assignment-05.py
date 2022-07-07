# write a python function that takes two lists and return True if they have at least
# one common num

#l=[1,2,3,4,5]
#l1=[6,9,7,8]
#l=set(l)
#l1=set(l1)

#ans=l.intersection(l1)
#if len(ans)==1:
   # print("True")
#else:
   # print("False")



l=[2,3,4,5,6]
l1=[1,6,7,8]
i=0
for i in range(len(l)):
    if l[i] in l1:
        print("True")
        break
    else:
        i=i+1
if i==len(l):
    print("False")

