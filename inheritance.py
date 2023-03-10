############################

# Single Inheritance

class Vehicle:
    def __init__(self, color, doors):
        self.color = color
        self.doors = doors


class Bike(Vehicle):
    def __init__(self, color, doors, wheels):
        self.wheels = wheels
        super().__init__(color, doors)


class Car(Vehicle):
    def __init__(self, color, doors, mileage):
        self.mileage = mileage
        super().__init__(color, doors)
    '''
    if we do add __init__ method in the child class then the __init__ 
    '''


honda = Bike('black', '0', '2')

mercize = Car('black', '4', '25')

print(honda.color)
print(honda.doors)
print(mercize.color)
print(mercize.doors)
print(mercize.mileage)
