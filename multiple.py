class X:
    def display(self):
        return "I am message from class X."


class A(X):
    b = 2
    # def display(self):
    #     return "I am message from class A."


class B:
    def display(self):
        return"I am message from B."

"""
This is multiple inheritance.
"""


class C(A, B):
    a = 1


obj = C()
print(obj.display())