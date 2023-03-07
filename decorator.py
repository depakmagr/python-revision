# @decorate_me
# def summ(a, b):
#     return a + b
#
#
#
# @decorate_me
# def diff(a, b):
#     return a - b
#
#
# print(summ(4, 5))
# print(diff(4, 5))
#
#
# #####################################
#
# def decorator_me(function):
#
#     def inner_func(a, b):
#         print("It is a decorated function.")
#         return function(a, b)
#
#     return inner_func
#
#
# @decorator_me
# def add(a, b):
#     return a + b
#
#
# # add = decorator_me(add)
# print(add(3, 5))
import time


####################

# def decorator_me(function):
#
#     def inner_func(*args, **kwargs):
#         print("It is a decorated function.")
#         return function(*args, **kwargs)
#
#     return inner_func
#
#
# @decorator_me
# def add(a, b, c):
#     return a + b + c
#
#
# # add = decorator_me(add)
# # print(add(3, 5, 1))
#
# import time
# start = time.time()
# print(add(3, 5, 1))
# end = time.time()
#
# print(f"Total function execution time is {end-start}")


#################################

def execute_time(func):
    def inner_function(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time() - start
        print(f"The function execution time is {end-start}")
        return r
    return inner_function


@execute_time
def message_print():
    time.sleep(5)
    # for i in range(1000000000):
    #     pass
    print("Hi !!!! Deos")


# message_print = execute_time(message_print)
message_print()