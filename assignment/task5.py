# Sort the given list of integers without using python method.

# a = [54, 1, 12, 99, 20, 13, 5, 100]             # output= [1, 5, 12,13, 20, 54, 99, 100]
#
# # Bubble sort algorithm
# n = len(a)
# for i in range(n):
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#
# print(a)



# for index, value in enumerate(a, start=1):       # Its takes value as given
#     print(index, value)
#####################

a = [54, 2, 99, 1, 20]
length = len(a)

for i in range(length - 1):
    for j in range(i + 1, length):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)


