# class Gurkul:
#     pass
#
#
# class Gurukul:
#     pass
#     s1=Gurkul()
#     s2=Gurkul()
#     print(s1)
#

# class student:
#     name = "Avinash"
#
# s1 = student()
# print(s1)
# print(s1.name)
# class Car:
#      brand = "Hyundai"
#      colour = "White"
# my_car=Car()
# print(my_car.brand)
# # class Car:
# #     brand = "Hyundai"
# #     colour = "White"
#
# # Create an instance of the Car class
# my_car = Car()
#
# # Print the details of the car
# print(f"Brand: {my_car.brand}")
# print(f"Colour: {my_car.colour}")

class Car:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour

    def display(self):
        print(f"car Details:\nbrand: {self.brand}\nModel: {self.model}\ncolour: {self.colour}")

#my_car = Car("toyota","s", "red")
my_car = Car("toyota","s", "red")
my_car.display()
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def display_details(self):
#         print(f"Car Details:\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}")
#
# # Creating an object of the Car class
# my_car = Car("Toyota", "Camry", 2020)
#
# # Displaying the details of the car
# my_car.display_details()