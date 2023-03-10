# class
#     camel case
#     CamelCase

#     snake case
#     Snake_Case

# ######################################
# class A:
#     a = 1
#     b = 2
#     def c(self, d):
#         print(d)
#         self.a
#
#
# obj = A()

########################################

# class Vehicle:
#     category = 'car'
#
#     def __init__(self, color, doors):
#         # color and doors are instance attributes
#         self.color = color
#         self.doors = doors
#
#     def description(self):
#         """
#         This method returns the description of the object.
#         """
#         return f"This vehicle's color is {self.color} and it has {self.doors} doors."
#
#     def make_it_blue(self):
#         """
#         change the color attributes to blue.
#         """
#         self.color = "blue"
#
#
# rover = Vehicle('red', '4')
# rolls = Vehicle('black', '5')
#
# print(f"before: {rover.color}")
#
# print(f"Vehicle color: {rover.color}")
#
# print(f"Vehicle category: {rover.category}")
# print(f"Number of doors: {rover.doors}")
#
# print(f"Category: {rover.__class__.category}")
# print(f"After {rover.color}")




#############################


class Electronics:

    category = 'mobile'

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def change_system(self):
        self.brand = "ISO"




phone = Electronics('Samsung', 'black')
phone1 = Electronics('Iphone','white')

print(f"Electronic category: {phone.category}")
print(f"Electronic brand: {phone.color}")
print(f"Electronic brand: {phone.brand}")
print(f"Electronic category: {phone1.category}")
print(f"Electronic brand: {phone1.color}")
print(f"Electronic brand: {phone1.brand}")





