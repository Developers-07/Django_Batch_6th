# map function
l=[1,2,3,4,5]
l1=[2,1,2,3,2]
def map_func(v, v1):
    return v+v1

x=map(map_func, l, l1)
print(x)
print(list(x))

# lambda function

getsum = lambda a,b:a+b if a+b>10 else "smaller than 10"
print(getsum(4,5))

#