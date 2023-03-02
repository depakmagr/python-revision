# Traversing

# WAP tp delete all the occurrences of a specified character in a given string

# s = "all the occurrences of a specified character in a given string."
# input = "a"
# output = "|| occurences of specified chrcter in given string."

s = "All the occurrences of a specified character in a given string."
a = input("Enter a character to be removed: ")
result = " "
for i in s:
    if i.lower() == a.lower():
        continue
    result += i   ## result = result + i  #Concatinate

print("Final result is:", result)






