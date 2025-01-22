# Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?
# class car:
#     def __init__(self, brand, model, year):
#         print(self)
#         self.brand=brand
#         self.model=model
#         self.year=year
#
# car1=car("lamborgini", "Lamborghini Revuelto", "2024")
# car2=car("verna", "Lamborghini Revuelto", "2024")
# print(car1.brand, car1.model, car1.year)
# print(car2.brand, car2.model, car2.year)
#
# Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?
# class student:
#     def __init__(self, name, roll_number, marks):
#         # Constructor to initialize the student's attributes
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks
#
#     def display_info(self):
#         # Method to display the student's details
#         print(self.name)
#         print(self.roll_number)
#         print(self.marks)
#
#
# # Example usage:
# student1 = student("Alice", 101, 95)
# student1.display_info()
#
# Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length= length
#         self.breadth= breadth
#
#     def area(self):
#         return self.length * self.breadth
#
#     def perimeter(self):
#         return 2 * self.length * self.breadth
#
# rec1= Rectangle(3,9)
# print(f"Area: {rec1.area()}")
# print(f"perimeter: {rec1.perimeter()}")
#
# Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?
#
# class Circle:
#     pi= 3.14
#     def __init__(self, radius):
#         self.radius=radius
#     def area(self):
#         return Circle.pi* self.radius* self.radius
#     def circumference(self):
#         return 2* Circle.pi* self.radius
# cir1=Circle(3)
# print(f"Area: {cir1.area()}")
# print(f"Circumference: {cir1.circumference()}")
#
# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
#
# class account:
#     def __init__(self, account_no, balance=0):
#         self.account_no = account_no
#         self.balance = balance
#     def debit(self, amount):
#         if amount>self.balance:
#             print("insufficient balance")
#         else:
#             self.balance-=amount
#             print(f"debited {amount}. New balance {self.balance}")
#     def credit(self, amount):
#         self.balance+=amount
#         print(f"credited amount is {amount}. New balance {self.balance}")
#
#     def print_balance(self):
#         print(f"account no {self.account_no}, balance: {self.balance}")
#
# account1=account("12345", 100)
# account1.print_balance()
# account1.credit(300)
# account1.debit(200)
# account1.print_balance()
#
# Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.
# class Employee:
#     # Class variable to keep track of the number of employees
#     employee_count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Employee.increment_employee_count()
#
#     @classmethod
#     def increment_employee_count(cls):
#         cls.employee_count += 1
#
#     @classmethod
#     def display_employee_count(cls):
#         print(f"Total Employees: {cls.employee_count}")
#
# # Example usage
# emp1 = Employee("Alice")
# Employee.display_employee_count()  # Outputs: Total Employees: 1
#
# emp2 = Employee("Bob")
# Employee.display_employee_count()  # Outputs: Total Employees: 2
#
# emp3 = Employee("Charlie")
# Employee.display_employee_count()  # Outputs: Total Employees: 3
#
# Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method.
# class Book:
#     def __init__(self, title, author, price=0):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def display_details(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: ${self.price:.2f}")
#
#
# # Example usage:
# book1 = Book("It ends with us", "Colleen Hoover ", 100)
#
#
# book1.display_details()
# print()
#
# Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.
# class TemperatureConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         return (celsius * 9/5) + 32
#
# converter = TemperatureConverter()
#
#
# temp1 = converter.celsius_to_fahrenheit(0)
# temp2 = converter.celsius_to_fahrenheit(25)
# print(f"10 degrees celcius= {temp1} Farenheit")
# print(f"25 degrees celcius= {temp2} Farenheit")
#
# Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum.
# class Time:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
#
#     def add_time(self, other):
#         # Add minutes and calculate carry over to hours
#         total_minutes = self.minutes + other.minutes
#         extra_hours = total_minutes // 60
#         final_minutes = total_minutes % 60
#
#         # Add hours and the carry over from minutes
#         total_hours = self.hours + other.hours + extra_hours
#
#         # Return a new Time object with the summed values
#         return Time(total_hours, final_minutes)
#
#     def display_time(self):
#         print(f"{self.hours} hours and {self.minutes} minutes")
#
#
# # Example usage:
# time1 = Time(2, 45)
# time2 = Time(1, 30)
#
# result = time1.add_time(time2)
#
# time1.display_time()
# time2.display_time()
# result.display_time()
#
# Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method set_bonus_percentage() to change the bonus percentage for all employees. Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.
# class EmployeeSalary:
#
#     basic_salary = 0
#     bonus_percentage = 0
#
#     def __init__(self, basic_salary):
#         self.basic_salary = basic_salary
#
#     def calculate_total_salary(self):
#         bonus = (self.basic_salary * EmployeeSalary.bonus_percentage) / 100
#         total_salary = self.basic_salary + bonus
#         return total_salary
#
#
#
# EmployeeSalary.bonus_percentage = 10
#
#
# employee1 = EmployeeSalary(3000)
# employee2 = EmployeeSalary(4500)
#
#
# print(f"Employee 1 Total Salary: ${employee1.calculate_total_salary():.2f}")
# print(f"Employee 2 Total Salary: ${employee2.calculate_total_salary():.2f}")