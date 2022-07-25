
# create file

file = open("file.txt", 'w') # 'w' stands for write
file.write("Hello brother ")
file.write("what is happening? ")
file = open("file.txt", 'r') # 'r' stands for read
# for i in file.readline():
#     print(i, end="")
print(file.read())


file = open("file.txt", 'a') # 'a' stands for append
file.write(" sorry man")


file.close()
