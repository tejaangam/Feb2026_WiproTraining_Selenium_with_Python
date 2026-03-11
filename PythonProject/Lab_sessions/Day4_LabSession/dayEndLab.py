#1.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter

class Circle:
    def radius(self, r):
        self.r = r
    def area(self):
        self.area = 3.14 * self.r * self.r
        print("Area of circle:", self.area)
    def perimeter(self):
        self.perimeter = 2 * 3.14 * self.r
        print("Perimeter of a circle:", self.perimeter)
print("1.Circle details:")
c = Circle()
c.radius(float(input(f"Enter the radius of the circle:")))
c.area()
c.perimeter()

#Write a Python program to create a person class. Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.

from datetime import datetime
class Person:
    def person_details(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    def calculate_age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(f"{self.name} is {age} years old.")   
print("2.Person details:")
p = Person()
name = input("Enter the name of a person:")
country = input("Enter the country of a person:")
dob =  input("Enter the date of birth of a person (YYYY-MM-DD):")  
p.person_details(name, country, dob)
p.calculate_age()   

#3.3.Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square.
class Shape:
    def area(self):
        pass
    def perimeter(self):    
        pass
class Circle(Shape):
    def circle_details(self, r):
        self.r = r
    def area(self):
        self.area = 3.14 *self.r *self.r
        print("Area of the circle: ", self.area)
    def perimeter(self):
        self.perimeter = 2 * 3.14 * self.r
        print("Perimeter of the circle: ", self.perimeter)
class Square(Shape):
    def square_details(self, side):
        self.side = side
    def area(self):
        self.area = self.side * self.side
        print("Area of the square: ", self.area)
    def perimeter(self):
        self.perimeter = 4 * self.side
        print("Perimeter of the square: ", self.perimeter)
class Triangle(Shape):
    def triangle_details(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        self.area = 0.5 * self.base * self.height
        print("Area of the triangle: ", self.area)
    def perimeter(self):
        self.perimeter = self.side1 + self.side2 + self.side3
        print("Perimeter of the triangle: ", self.perimeter)
print("3.Shape details:")
c = Circle()
c.circle_details(float(input("Enter the radius of the circle:")))
c.area()
c.perimeter()

s = Square()
s.square_details(int(input("Enter the side length of the square:")))
s.area()
s.perimeter()

t = Triangle()
t.triangle_details(float(input("Enter the base of the triangle:")), float(input("Enter the height of the triangle:")), float(input("Enter side 1 of the triangle:")), float(input("Enter side 2 of the triangle:")), float(input("Enter side 3 of the triangle:")))
t.area()
t.perimeter()   


#4.Write a python program to create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def Vehicle_details(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class Bus(Vehicle):
    def bus_details(self, capacity):
        self.capacity = capacity
    def display_bus_details(self):
        self.display_details()  # Call the parent class method to display vehicle details
        print(f"Capacity: {self.capacity} passengers")
print("4.Bus details:")
b = Bus()
b.Vehicle_details(input("Enter the brand of the bus: "), input("Enter the model of  the bus: "), int(input("Enter the year of the bus: ")))
b.bus_details(int(input("Enter the capacity of the bus: ")))
b.display_bus_details() 
5

