# class X:
#     def display(self):
#         return "I am message from class X."
#
#
# class A(X):
#     b = 2
#     # def display(self):
#     #     return "I am message from class A."
#
#
# class B:
#     def display(self):
#         return"I am message from B."
#
# """
# This is multiple inheritance.
# """
#
#
# class C(A, B):
#     a = 1
#
#
# obj = C()
# print(obj.display())
# print(obj.a)


# Inheritance
# Encapsulation
# Polymerphism



# giving permission to the user is encapsulation

'''
        Types of Encapsulation
        public =
        private = __a = 1 with in the class only.
        protected = cannot use outside from class   _a = 1 to variable and class
'''


# Protected
# class Vehicle:
#     def __init__(self):
#         self.color = "black"
#         '''This is protected member.'''
#         self._mileage = 90
#
#     def change_mileage(self, mileage):
#         self._mileage = mileage
#
#
#
# my_vehicle = Vehicle()
# print(my_vehicle._mileage)
# my_vehicle.change_mileage(25)
# print(my_vehicle._mileage)
#
#
#
# """This is also possible but not recommended"""
# my_vehicle._mileage = 10
# print(my_vehicle._mileage)




# private
class Vehicle:
    def __init__(self):
        self.color = "black"
        '''This is protected member.'''
        self.__mileage = 90

    def change_mileage(self, mileage):
        self._mileage = mileage



my_vehicle = Vehicle()

"""Cannot access private members in this way"""
print(my_vehicle.__doors)

'''Can access protected member in this way but not recommended'''
print(my_vehicle._mileage)

'''This is called name mangling. Cana access even the private members'''
print(my_vehicle._Vehicle__doors)

