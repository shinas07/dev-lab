# Inheritance in Python
"""Python inheritance allow us to create a new class that uses the feature of an exisiting class. It help us resue code and build relationships between classes"""

# Syntax
class Parent:
    # parent class code
    pass

class Child(Parent):
    # child class code
    pass


"""Python offer various types of inheritance based on the number of child and paren classes involed in the inheritance"""
"""
1. Single Inheritance 
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance 
"""

"""Signle Inheritance: A class inherits from one parent class"""
# Parent class ----> Child class

# Example:
class Person:
    def display_name(self):
        print("Name : Shinas")

class Student(Person):
    def display_course(self):
        print("Course: Python Programming")

s = Student()
s.display_name()
s.display_course()


# Single Inheritance (With super and init)
class User:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Generic user"
    
class Admin(User):
    def __init__(self, name, level):
        super().__init__(name) # pull parent logic
        self.level = level

    def get_role(self):
        return f"Admin (Level {self.level})"

u = Admin("Shinas", 3)
print(u.name)
print(u.get_role())
    

""" Multiple Inheritance: A single subclass Inherits from multiple super class so the child class can access the attributes and method from two or more parent classes"""
# Parent Class1 --- \⌄
#                    Child Class
# Parent Class2 ----/^
print("------------Multiple Inheritance------------")

# Example 
class Teacher:
    def teach(self):
        print("Teaches Math and Science")

class Coach:
    def train(self):
        print("Trains in Football and Athletics")

class Student(Teacher, Coach):
    def activites(self):
        print("Student is active in both academics and sports")
        self.teach()
        self.train()

s = Student()
s.activites()


"""Multilevel Inheritance: A class that inherits from a child class which itself inherits from anther parent class"""

# Grandparent Class ---> Parent class ---> Child Class
print("------------Multilevel Inheritance------------")

class Grandparent:
    def show_grandparent(self):
        print("Grandparent: shares wisdom")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent: Provides guidence")

class Child(Parent):
    def show_child(self):
        print("Child: Learn and grows")


c = Child()
c.show_grandparent()
c.show_parent()
c.show_child()


"""Hierarchical Inheritance: It is actully the opposite of multiple inheritance. Therefore, more the one child class can be derived from a single-parent class."""
                # Child Class
# Parent Class ----|
                # Child Class
print("------------Hierarchical Inheritance------------")
class Animal:
    def sound(self):
        print("Animal make different sound")

class Dog(Animal):
    def bark(self):
        print("Dog: Barks")

class Cat(Animal):
    def meow(self):
        print("Cat: Meows")

# Creating objects of both child classes
d = Dog()
d.sound()
d.bark()

c = Cat()
c.sound()
c.meow()   

"""Hybrid Inheritance: Is combines two or more type of inheritance. we can say that hybrid inheritance in Python is a mixture of more than one inheritance style. like single. multiple, or multilevel."""
print("------------Hybrid Inheritance------------")
# Base class
class Vehicle:
    def show_type(self):
        print("Vehicle: User for transportation")

# First level child (single inheritance)
class Car(Vehicle):
    def car_features(self):
        print("Car: Has 4 wheels and AC")
    
# Another base class for multiple inheritance
class Electric:
    def batter_info(self):
        print("Electric: Runs on battery")

class ElectricCar(Car, Electric):
    def features(self):
        print("ElectricCar: Eco-friendly and silent")


# Create object of ElectricCar

ecar = ElectricCar()
ecar.show_type()
ecar.car_features()
ecar.batter_info()
ecar.features()
print(f"Method Resolution Order: {ElectricCar.mro()}")  # This helps us to understand how python decides which parent method to call first

"""super function: It allow us to access method and properites of parent class from a child class"""
print("------------super()------------")

# Example:
class Vehicle:
    def __init__(self):
        print("Vehicle is ready")

class Car(Vehicle):
    def __init__(self):
        super().__init__()  # Calls the parent class constructor
        print("Car is ready")

c = Car()

print("------------Object Composition------------")
"""Composition: has-a relationshiop"""
# Car has-a Engine

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine() # Composition (Car has-an Engine)

    def start(self):
        self.engine.start()
        print("Car is running")

my_car = Car()
my_car.start()

