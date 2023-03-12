# Function overloading

# def addition(a, b):
#     return a + b
#
#
# def addition(a, b, c):
#     return a + b + c
#
# # print(addition(1, 2))
# print(addition(1, 2, 3))


########################################
# Method Overloading
#
# class Shape:
#     def area(self, l):
#         return l*l
#
#     def area(self, l, b):
#         return l*b
#
#
# square = Shape()
# print(square.area(5))


#################################

# class Shape:
#     def area(self, l, b=None):
#         if b is not None:
#             return l*b
#         return l*l
#
#
# square = Shape()
# print(square.area(5))
# print(square.area(2, 4))


#################################

# Class Method

# class Vehicle:
#     category = 'car'
#
#     @classmethod
#     def printCategory(cls):
#         print(f"Vehicle category = {cls.category}")
#
#
# Vehicle.printCategory()
#
# my_vehicle = Vehicle()
# my_vehicle.printCategory()


##########################################################

# Factory Method

# from datetime import date
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     def display(self):
#         print(f"{self.name} is {self.age} years old.")
#
#
# obj = Person("Deeps", 24)
# obj.display()
#
# obj1 = Person.fromBirthYear("Deps", 1998)    # Factory Method
# obj1.display()


####################################

#Static Method

class Vehicle:
    @staticmethod
    def is_good_mileage(mileage):
        if mileage < 25:
            return "No"
        return "Yes"


print(Vehicle.is_good_mileage(25))
print(Vehicle.is_good_mileage(15))



