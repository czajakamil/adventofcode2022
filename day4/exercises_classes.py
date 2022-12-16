"""
1. Create a simple class called "Person" that has two attributes: "name" and "age". Then, create a method called "greet" that prints a greeting using the person's name.

2. Modify the "Person" class from the previous exercise to include a third attribute called "height" and a method called "is_tall" that returns True if the person's height is over a certain threshold (you can choose the threshold).

3. Create a subclass of the "Person" class called "Student" that has an additional attribute called "student_id" and a method called "enroll" that prints a message about enrolling in a course.

4. Write a program that creates a list of "Person" objects and a list of "Student" objects, then use a for loop to iterate over each list and call the greet method for each object.
"""

class Person:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.age = age
        self.height = height

    def geet(self):
        greeting = f"Hello {self.name}, nice to see you. You are {self.age} years old, right?"
        return greeting

    def is_tall(self, threshold):
        return "tall" if self.height >= threshold else "short"

class Student(Person):
    def __init__(self, name, age, height, student_id):
        # This line calls Person class using super().__init__ and adds student_id atribute
        super().__init__(name, age, height)
        self.student_id = student_id

    def enroll(self):
        print(f"{self.name} with id {self.student_id} has been enrolled in a course")

name = input("What's your name? ")
age = input("What's your age? ")
height = int(input("What's your height? "))


p = Person(name, age, height)
print(f"{p.name} is {p.is_tall(170)}")

print(p.geet())

# Create a list of Person objects
people = [
    Person("Kamil", 25, 178),
    Person("John", 30, 170),
    Person("Mary", 20, 160),
    Person("Bob", 40, 190),
    Person("Alice", 50, 150)
    ]

# Create a list of Student objects
students = [
    Student("Kamil", 25, 178, 123456),
    Student("John", 30, 170, 654321),
    Student("Mary", 20, 160, 987654),
    Student("Bob", 40, 190, 456789),
    Student("Alice", 50, 150, 321987)
    ]

# Iterate over the people list and call the greet method for each object
for person in people:
    print(person.geet())

# Iterate over the students list and call the greet method for each object
for student in students:
    print(student.geet())

# Iterate over the students list and call the enroll method for each object
for student in students:
    student.enroll()