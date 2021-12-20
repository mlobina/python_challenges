from datetime import datetime


def check_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper

# # если декоратор принимает аргумент
# def check_time(arg):
#     print(arg)
#
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             start = datetime.now()
#             result = func(*args, **kwargs)
#             print(datetime.now() - start)
#             return result
#
#         return wrapper
#
#     return outer


@check_time
def one(n):
    lst = []
    for i in range(n):
        if i % 2 == 0:
            lst.append(i)
        else:
            pass
    return lst


@check_time
def two(n):
    lst = [i for i in range(n) if i % 2 == 0]
    return lst



