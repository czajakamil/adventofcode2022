"""
1. Create a Shape class that has a name attribute and a num_sides attribute. Then, create subclasses for specific shapes, such as Triangle, Square, and Circle. Each subclass should have a __init__ method that initializes the name and number of sides of the shape, and a method called area that calculates the area of the shape.

2. Create a BankAccount class that has a balance attribute and a withdraw method that allows you to withdraw money from the account. The method should check that the account has sufficient funds before allowing the withdrawal. Also, create a deposit method that allows you to deposit money into the account.

3. Create a Car class that has a make attribute and a model attribute. Then, create a Dealership class that has a list of Car objects and a method called inventory that prints the make and model of each car in the dealership's inventory.

4. Create a Point class that has x and y attributes. Then, create a Line class that has two Point objects as attributes and a method called length that calculates the length of the line.

5. Create a Person class that has a name attribute and a friends attribute that is a list of Person objects. Then, create a Network class that has a list of Person objects and a method called add_friend that allows you to add a friend to a person's list of friends. Also, create a num_friends method that calculates the total number of friends a person has in the network.
"""

class Shape:
    def __init__(self, name: str, num_sides: int):
        self.name = name
        self.num_sides = num_sides

class Triangle(Shape):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().__init__("Triangle", 3)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

class Square(Shape):
    def __init__(self, side: int):
        super().__init__("Square", 4)
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__("Circle", 0)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

kk = Triangle(3, 4, 5).area()

print(kk)