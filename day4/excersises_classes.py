"""
1. Create a simple class called "Person" that has two attributes: "name" and "age". Then, create a method called "greet" that prints a greeting using the person's name.

2. Modify the "Person" class from the previous exercise to include a third attribute called "height" and a method called "is_tall" that returns True if the person's height is over a certain threshold (you can choose the threshold).

3. Create a subclass of the "Person" class called "Student" that has an additional attribute called "student_id" and a method called "enroll" that prints a message about enrolling in a course.

4. Write a program that creates a list of "Person" objects and a list of "Student" objects, then use a for loop to iterate over each list and call the greet method for each object.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def geet(self):
        greeting = f"Hello {self.name}, nice to see you. You are {self.age} years old, right?"
        return greeting


name = input("What's your name? ")
age = input("What's your age? ")

p = Person(name, age)

print(p.geet())
