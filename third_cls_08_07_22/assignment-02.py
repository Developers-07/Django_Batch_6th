# write a program to get a string made of the first 2 and last 2 chars
# from a given string.for example: input->assignment output->asnt

#s=input("Enter the string : ")
#l=len(s)
#s1=s[:2]
#s2=s[l-2:l]
#print(s1+s2)

s=input("Enter the string : ")
l=len(s)
st=""
for i in range(l):
    if i==0 or i==1:
        st=st+s[i]
    if i==l-2 or i==l-1:
        st=st+s[i]
print(st)

