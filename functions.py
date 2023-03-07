#defining the function

# def messege(text):
#     print("This is {text} from the function")
#
# messege("Using")
#
#
# def square_a_num(value):
#     return value ** 2


################################

# Create a new list

# def custom_sort(a):
#     length = len(a)
#
#     for i in range(length - 1):
#         for j in range(i + 1, length):
#             if a[i] > a[j]:
#                 a[i], a[j] = a[j], a[i]
#     return a
#
#
#
# a = [54, 2, 99, 1, 20]
# result = custom_sort(a)
# print(result)



########################

# def deepak(n):
#     new = 0
#     for i in n:
#         new = new * 10 + i
#
#     print(new)
#     return n
#

# n = [1, 2, 3, 4]
# dis = deepak(n)
# print(dis)


#############################

# def deeps(a):
#     length = len(a)
#     for i in range(length - 1):
#         for j in range(i + 1, length):
#             if a[i] > a[j]:
#                 a[i], a[j] = a[j], a[i]
#     print(a)
#
# a = [1,27,3,45,5]
# b = [6,7,88,9,160]
# deeps(a)
# deeps(b)





##########################

# Create a new list of repeated items in a provided list.

def repeated_items(nums):
    result = []
    for i in nums:
        if nums.count(i) > 1 and i not in result:
            result.append(i)
    return result



nums = [3, 4, 2, 2, 11, 3, 3, 3, 4]
result = repeated_items(nums)
print(result)



#############################
