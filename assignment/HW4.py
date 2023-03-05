# Write a program to check whether a string is anagram or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "silent" and "listen" are an anagram of each other.

def is_anagram(str1, str2):
    # Convert both strings to lowercase and remove all spaces
    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')

    # Check if the two strings have the same length
    if len(str1) != len(str2):
        return False

    # Convert each string to a list of characters, sort them, and convert back to a string
    str1_sorted = ''.join(sorted(list(str1)))
    str2_sorted = ''.join(sorted(list(str2)))

    # Compare the sorted strings
    if str1_sorted == str2_sorted:
        return True
    else:
        return False

# Test the function with some examples
print(is_anagram("silent", "listen"))  # True
print(is_anagram("restful", "fluster"))  # True
print(is_anagram("hello", "world"))  # False


git add .
git commit -m "assignments"
git branch -M main
git push -u origin main