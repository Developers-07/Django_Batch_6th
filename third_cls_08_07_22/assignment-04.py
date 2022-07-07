# write a python program to remove duplicates from a list

#l=[3,4,2,8,3,5,2,3]
#s={1}
#for i in range(len(l)):
   # s.add(l[i])
#s.remove(1)
#print(s)

#l=[2,5,6,3,2,5,3,10]
#print(list(set(l)))

l=[2,5,6,4,2,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

