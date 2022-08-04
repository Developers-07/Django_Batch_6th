
# try:
#     n = 110
#     if n > 100:
#         raise Exception
# except Exception as e:
#     print("Exception is working")

try :
     # if we type  10 , it will show typeerror
    # n = input("Enter the Name = ")
    # print(n)

     # if we type string , it will show valueerror
     # n = int(input("Enter the value = "))
     # print(n/2)

     # otherwise
     n = int(input("Enter the value = "))
     print(n/0)

except ValueError as e:
   print("The ValueError is happened =", e)
except TypeError as e:
   print("The TypeError is happened =", e)
except Exception as e:
    print("The Error is =", e)