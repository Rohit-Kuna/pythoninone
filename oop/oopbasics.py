############################################################
# 🎯 OBJECT-ORIENTED PROGRAMMING (OOP) PRACTICE SHEET
# Follow the instructions and complete the exercises 💪
############################################################


############################################################
# 1️⃣ CREATING A CLASS
############################################################

# TODO: Create a class named Person (empty class first)
class Person:
    pass


############################################################
# 2️⃣ ADDING A CONSTRUCTOR (__init__)
############################################################

# TODO: Modify Person class to accept name and age
# and store them as properties/attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


############################################################
# 3️⃣ CREATING OBJECTS
############################################################

# TODO: Create two Person objects - p1 and p2
p1 = Person("Rohit", 25)
p2 = Person("Anya", 22)


############################################################
# 4️⃣ ADD A METHOD TO CLASS
############################################################

# TODO: Add a method greet() inside Person class that prints:
# "Hello, my name is <name>"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("Rohit", 25)
p2 = Person("Anya", 22)
p1.greet()
p2.greet()


############################################################
# 5️⃣ ACCESS AND MODIFY OBJECT ATTRIBUTES
############################################################

# TODO: Print name and age of both objects
print(p1.name, p1.age)
print(p2.name, p2.age)

# TODO: Change age of p1 to a new value and print again
p1.age = 26
print(p1.name, p1.age)


############################################################
# 6️⃣ ENCAPSULATION (PRIVATE ATTRIBUTES)
############################################################

# Create a class BankAccount
# Private attribute: __balance
# Methods:
#   deposit(amount) → add to balance
#   get_balance() → return balance

# TODO: Implement BankAccount class fully
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())


############################################################
# 7️⃣ CLASS VS INSTANCE ATTRIBUTES
############################################################

# Create a class Car with:
# Class attribute: wheels = 4 (common to all cars)
# Instance attributes: brand, color (different for each car)
#
# TODO: Show difference by printing:
# Car.wheels and car1.wheels
class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Tesla", "Red")
print(Car.wheels)
print(car1.wheels)


############################################################
# 8️⃣ CLASS METHODS & STATIC METHODS
############################################################

# Add two methods inside class Car:
# @classmethod → change value of wheels
# @staticmethod → print "Cars are awesome!"
#
# TODO: Write and test both
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def change_wheels(cls, num):
        cls.wheels = num

    @staticmethod
    def info():
        print("Cars are awesome!")

Car.change_wheels(6)
print(Car.wheels)
Car.info()


############################################################
# 9️⃣ INHERITANCE
############################################################

# Create a Parent class Animal with method speak()
# Create a Child class Dog that inherits Animal
# Override speak() → print "Dog barks"
#
# TODO: Demonstrate calling methods on Dog object
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()


############################################################
# 🔟 POLYMORPHISM
############################################################

# Create 2 different classes: Cat and Cow
# Both have speak() method (different outputs)
# Write a function make_sound(animal) that calls speak()
#
# TODO: Test with Cat and Cow objects
class Cat:
    def speak(self):
        print("Cat meows")

class Cow:
    def speak(self):
        print("Cow moos")

def make_sound(animal):
    animal.speak()

make_sound(Cat())
make_sound(Cow())


############################################################
# 1️⃣1️⃣ ABSTRACTION (Optional Advanced)
############################################################

# Use abc module to create an abstract class Shape
# with method area()
# Create subclasses: Circle, Rectangle
# Implement area() accordingly
#
# TODO: Create objects and print areas
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

print(Circle(5).area())
print(Rectangle(4, 6).area())


############################################################
# 🎉 BONUS PRACTICAL QUESTIONS
############################################################

# Q1: Create Student class with marks → Add method get_grade()
# If marks >= 90: A, >= 75: B, >= 50: C, else Fail
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_grade(self):
        if self.marks >= 90: return "A"
        elif self.marks >= 75: return "B"
        elif self.marks >= 50: return "C"
        else: return "Fail"

print(Student("Rohit", 82).get_grade())

# Q2: Create a class Counter where each new object increments a counter
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

c1 = Counter(); c2 = Counter(); c3 = Counter()
print(Counter.count)

# Q3: Create a Library class
# Features:
#   Add book
#   Remove book
#   Check if book exists
#   Show total books
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, b):
        self.books.append(b)
    def remove_book(self, b):
        if b in self.books:
            self.books.remove(b)
    def has_book(self, b):
        return b in self.books
    def total_books(self):
        return len(self.books)

lib = Library()
lib.add_book("Python OOP")
print(lib.has_book("Python OOP"))
print(lib.total_books())


############################################################
# END OF PRACTICE SHEET 🚀
############################################################