# write a python program to get a largest number from a list

l=[]
for i in range(5):
    p=int(input("Take input in a list "))
    l.append(p)
print(l)

#l.sort()
#print(l[4])

l.sort()
l.reverse()
print("Largest number of this list =",l[0])