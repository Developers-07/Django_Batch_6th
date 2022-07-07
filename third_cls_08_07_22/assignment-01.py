# Find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string

s="He is not a poor man"
f=s.find("not")
l=s.find("poor")
if f<l and f>0:
    s=s.replace(s[f:l+4],"good")
else:
    s=s
print(s)

