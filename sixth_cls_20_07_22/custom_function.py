# def custom_function(*args, **kwargs):
#     print(args)
#
# custom_function(1, 2, 3, 4, 5)


def custom_function(*args, **kwargs):
    print(kwargs)

custom_function(a=1, b=2, c=3, d=4, e=5)

# Difference between return & yield
# return
def get_num():
    for i in range(5):
         return i

print(get_num())

# yield
def get_num():
    for i in range(5):
        yield i

print(list(get_num()))
