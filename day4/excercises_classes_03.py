"""
1. Create a class called "Person" that stores a person's name, age, and occupation. Add a method called "introduce" that prints a string introducing the person, including their name and occupation.
"""

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation


    def __str__(self) -> str:
        return f"Hi, {self.name}, how are you? Are you still working as an {self.occupation}?"

p = Person("Kamil", 22, "Bussiness Analyst")
print(p)

"""

"""