
try:
    file = open("test.txt", 'w')  # here we have to use 'r' to readable
    for i in file:
        print(i, end=" ")

except Exception as e:
    print("The Error is =", e)




# file = open("test.txt", 'w')
# file.write("Hy Sobuz vi whats upp")
#
# file = open("test.txt", 'r')
# print(file.read())
#
# file = open("test.txt", 'a')
# file.write(" rahim mia")
#
# file = open("test.txt", 'r')
# for i in file.readline():
#     print(i, end='')
#
# file.close()




#try :
#     print("My Project is Done")
#     val = 10/0
#     print(val)
#
# except Exception as e :
#     print("The Error is =", e)
#
# finally :
#     print("We can able to find out the error")