# Create a class Department with parameters name and number_of_students. Create a method total students, which takes object as a parameter and return the number of students from all departments.

# class Department:
#     def __init__(self, name, num_of_stds):
#         self.name = name
#         self.num_of_stds = num_of_stds
#
#     def total_stds(self, obj):
#         return self.num_of_stds + obj.num_of_stds
#
#
#
# d1 = Department("Sports", 20)
# d2 = Department("Account", 12)
# result = d1.total_stds(d2)
# print(result)



############################

# class Department:
#     def __init__(self, name, num_of_stds):
#         self.name = name
#         self.num_of_stds = num_of_stds
#
#     def total_stds(self, *args):
#         list_of_nums = sum[[i.num_of_stds for i in args]]
#         other_total = sum(list_of_nums)
#         return self.num_of_stds + other_total
#
#
# d1 = Department("Sports", 20)
# d2 = Department("Account", 12)
# d3 = Department("Sports", 30)
# d4 = Department("Account", 42)
# d5 = Department("Sports", 40)
# d6 = Department("Account", 11)
# result = d1.total_stds(d1, d2, d3, d4, d5, d6)
# print(result)




#############################

"""
    Create a class Cricketer that has the properties name, age and number of match played. Create another class Batsman that
    inherits class Cricketer with properties number of runs and number of centuries. Similarly, create another class Bowler 
    that inherits the class Cricketer with property number of wickets.
    Create get_info{} method in each class that prints the information accordingly.
"""


class Cricketer:
    def __init__(self, name, age, number_of_match_played):
        self.name = name
        self.age = age
        self.number_of_match_played = number_of_match_played

    def get_info(self):
        return(f"The Cricketer {self.name} is {self.age} years old who have played {self.number_of_match_played} matches.")


class Batsman(Cricketer):
    def __init__(self, name, age, number_of_match_played, num_of_runs, num_of_cents):
        self.num_of_runs = num_of_runs
        self.num_of_cents = num_of_cents
        super().__init__(name, age, number_of_match_played)

    def get_info(self):
        return(f"The Cricketer {self.name} is {self.age} years old who have played {self.number_of_match_played} matches and make {self.num_of_runs} runs and {self.num_of_cents} centuries.")


class Bowler(Cricketer):
    def __init__(self, name, age, number_of_match_played, num_of_wickets):
        self.num_of_wickets = num_of_wickets
        super().__init__(name, age, number_of_match_played)

    def get_info(self):
        return(f"The Cricketer {self.name} is {self.age} years old who have played {self.number_of_match_played} matches and successful to make break {self.num_of_wickets} wickets.")


obj = Cricketer("Gabs", 23, 80)
print(obj.get_info())

obj1 = Bowler('Noob', 1, 12, 4)
print(obj1.get_info())

obj2 = Bowler('Deeps', 19, 15, 13)
print(obj2.get_info())







git add .
git commit -m "assignments"
git branch -M main
git push -u origin main