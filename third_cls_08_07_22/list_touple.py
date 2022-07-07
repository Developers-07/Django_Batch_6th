#list,touple,set,dictionary

# list(mutable)

l=[1,2,3,5.5,2,4.5,"zishan","disha"]
l.append("synthia")
print(l)

l.insert(8,"rini")
print(l)

l.pop()
print(l)

c=l.count(2)
print(c)

i=l.index("zishan")
print(i)

print("*"*30)

lis=[3,5,1,9,3,6,10]
lis.sort()
print(lis)

lis.reverse()
print(lis)

print("*"*30)

# nested list

nlis=[[1,2,[1,4,8],3,4],[3,5,7],[10,20,30]]
print(nlis)
print(nlis[1][1])
print(nlis[0][2][1])

print("*"*30)

# touple(immutable)

t=(1,3,5,7,9)
print(t)
# not changeable
#t[3]=10
#print(t)