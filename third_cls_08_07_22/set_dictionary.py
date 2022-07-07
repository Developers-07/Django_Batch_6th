# set
# immutable, no-indexing

s={}
print(type(s))

s={1,2,3,4,5,2,5}
print(type(s))
s.add(10)
print(s)
s.remove(4)
print(s)
print("*"*30)

s2={6,7,8,9}
s3={3,6,7,2,9,8}

print(s2.union(s3))
print(s.intersection(s3))
print(s2.issubset(s3))
print(s3.issubset(s2))
print("*"*30)




