
try:
    # logic statement
    print("welcome")
    val = 10
    print(val*10)

    str = "10"
    print(str / 2)

    ans=val/0
    print(ans)

except Exception as e:
    # show what type of Error

    print("Error is = ",e)


a = 100/10
print(a)


# try:
#     print("Welcome to Exception Handling")
#     n = input("Enter your name : ")
#     ans = n/2
#     print(ans)
#
#     v = 10/0
#     print(v)
#
# except Exception as e:
#     print("The Error is = ", e)
