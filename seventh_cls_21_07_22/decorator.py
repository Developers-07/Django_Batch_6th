# all about decorator

# def func1():
#     print("Function one is called")
# func2=func1
# del func1
# func2()

# def test(num):
#     if num==0:
#         return sum
#     else:
#         return print
# res=test(10)
# print(res)

# def test(func):
#     func("Are you surprised?")
# test(print)

# def decorator_func(func):
#     def new_func():
#         print("print first line")
#         func()
#         print("print second line")
#     return new_func
#
# def func1():
#     print("Learning Decorator is amazing")
#
# func1=decorator_func(func1)
# func1()


def decorator_func(func):
    def wrapper_func():
        print("wrapper_func is worked")
        return func()
    print("decorator_func is worked")
    return wrapper_func

@decorator_func
def show():
    print("show is worked")
#show=decorator_func(show)
show()