# "Python+is+an+awesome+language". Split the given string to get a list and join to get another string "Python is an awesome language."

given_str = "Python + is + an + awesome + language."

# Split the string into a list using the "+" delimiter
str_list = given_str.split("+")

# Join the list back into a string using " " (space) as the delimiter
new_str = " ".join(str_list)

print(new_str)

# a = "Python + is + an + awesome + language."
# l = a.split("+")
# l = [i.strip() for i in l]
# print(l)
# s = " ".join(l)
# print(s)
