# Static Methods
# Create a class MathOperations that contains:
# A static method add_numbers that takes two arguments and returns their sum.
# A static method multiply_numbers that takes two arguments and returns their product.

# class MathOperations:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     @staticmethod
#     def mul(a,b):
#         return a*b
# result_sum = MathOperations.add(2,4)
# result_product = MathOperations.mul(2,4)
#
# print(result_sum)
# print(result_product)

# Class Methods
# Create a class Person that keeps track of the number of people created. The class should have:
# A class variable count to count instances of the class.
# A class method get_count that returns the current count.

# class Person:
#     count=0
#     def __init__(self):
#         Person.count+=1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# person1=Person()
# person2=Person()
# person3=Person()
#
# print(f"the number of people created: {Person.get_count()}")

# Using Both Static and Class Methods
# Create a class TemperatureConverter with the following:
# A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
# A class method info that returns a message about temperature conversions.

# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32
#     @classmethod
#     def info(cls):
#         return 'This class provides coversion from celcius to farenheit'
#
# temp = TemperatureConverter.celsius_to_fahrenheit(30)
# msg =  TemperatureConverter.info()
#
# print(f" 30 degrees Celsius in farenheit is: {temp} degrees F")
# print(msg)

# Single Inheritance
# Create two classes:
# Animal with a method sound that prints "Animal sound".
# Dog that inherits from Animal and overrides the sound method to print "Bark".
# class Animal:
#     def sound(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
# # Example usage:
# animal = Animal()
# animal.sound()
#
# dog = Dog()
# dog.sound()

# Multiple Inheritance
# Create two classes:
# Bird with a method fly that prints "Flying".
# Fish with a method swim that prints "Swimming".
# A class Duck that inherits from both Bird and Fish.
# class Bird:
#     def fly(self):
#         print("Flying")
#
# class Fish:
#     def swim(self):
#         print("Swimming")
#
# class Duck(Bird, Fish):
#     def quack(self):
#         print("Quack")
#
# # Example usage:
# duck = Duck()
# duck.fly()   # Output: Flying
# duck.swim()  # Output: Swimming
# duck.quack() # Output: Quack

# Abstract Class
# Use the abc module to create an abstract class Shape that contains:
# An abstract method area().
# Two concrete classes Circle and Rectangle that inherit from Shape and implement the area method.

# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# # Example usage:
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
#
# print(f"Area of the circle: {circle.area():.2f}")
# print(f"Area of the rectangle: {rectangle.area()}")

# Encapsulation
# Create a class BankAccount that uses encapsulation:
# Private attributes _balance.
# Public methods deposit() and withdraw() that modify _balance safely.
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance  # Private attribute
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: ${amount:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrew: ${amount:.2f}")
#         else:
#             print("Withdrawal amount must be positive and cannot exceed the current balance.")
#
#     def get_balance(self):
#         return self._balance
#
# # Example usage:
# account = BankAccount(100)  # Create an account with an initial balance of $100
# print(f"Initial Balance: ${account.get_balance():.2f}")
#
# account.deposit(50)          # Deposit $50
# print(f"Balance after deposit: ${account.get_balance():.2f}")
#
# account.withdraw(30)         # Withdraw $30
# print(f"Balance after withdrawal: ${account.get_balance():.2f}")
#
# account.withdraw(150)        # Attempt to withdraw more than the balance


# Polymorphism with Method Overriding
# Create two classes Cat and Dog with a method speak().
# The Dog class should implement speak() to print "Woof".
# The Cat class should implement speak() to print "Meow".
# class Animal:
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow")
#
# # Example usage:
# animals = [Dog(), Cat()]
#
# for animal in animals:
#     animal.speak()


def product(a, b):
    p = a * b
    print(p)

# Second product method
# Takes three argument and print their
# product

# Polymorphism with Method Overloading
# Create a class Calculator with a method add() that:
# Can accept 2 or 3 arguments and returns their sum.
# Hint: Use default parameters to handle method overloading in Python.
# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
#
# # Example usage:
# calc = Calculator()
#
# # Adding two numbers
# result1 = calc.add(5, 3)
# print(f"Sum of 5 and 3: {result1}")  # Output: Sum of 5 and 3: 8
#
# # Adding three numbers
# result2 = calc.add(5, 3, 2)
# print(f"Sum of 5, 3, and 2: {result2}")  # Output: Sum of 5, 3, and 2: 10

# Multilevel Inheritance
# Create three classes:
# LivingBeing with a method breathe() that prints "Breathing".
# Mammal that inherits from LivingBeing and adds a method walk() that prints "Walking".
# Human that inherits from Mammal and adds a method think() that prints "Thinking".
# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
#
# class Mammal(LivingBeing):
#     def walk(self):
#         print("Walking")
#
# class Human(Mammal):
#     def think(self):
#         print("Thinking")
#
# # Example usage:
# human = Human()
# human.breathe()  # Output: Breathing
# human.walk()     # Output: Walking
# human.think()    # Output: Thinking