#############################
# Function inside function.

# def func(name):             # normal function with name as argument.
#     return "Hello " + name.upper() + '.'
#
#
# def greet(my_func):                 # function with another function as argument.
#     messege = my_func('deps')               # calling the passed function
#     print(messege)
#
#
# greet(func)


################################

def greet(msg):

    def print_message():
        print(msg)

    return print_message


message = greet("Hiiiiiii! Deos.")
message()