#1.Create a Car class with attributes brand, model, price.

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


car = Car("Toyota", "Fortuner", "3000000")

print(car.brand)
print(car.model)
print(car.price)


#2.Create a Student class with method get_grade() based on marks.
class Student:
    def __init__(self, name, marks):
        self.marks = int(marks)
        self.name = name
    def get_grade(self):

        if self.marks >= 90:
            return "A-Grade"
        elif self.marks >= 75:
            return "B-Grade"
        elif self.marks >= 50:
            return "C-grade"
        else:
            return "fail"
stu1 = Student("teja", "95")
print("Name:", stu1.name)
print("Marks:", stu1.marks)
print("Grade:", stu1.get_grade())

#Create a BankAccount class with deposit() and withdraw() methods.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
acc = BankAccount("Teja", 5000)
acc.deposit(1000)
acc.withdraw(200)
print("Current balance", acc.balance)

#Write a class Employee that initializes name, id, salary using __init__.
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

emp1 = Employee("Teja", "45", "400000")

print("Name of an employee:", emp1.name)
print("Id:", emp1.id)
print("Salary(in Rs):", emp1.salary)

#Create a class that counts how many objects are created.
class Counter:
    count = 0   # class variable
    def __init__(self):
        Counter.count += 1
# Creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
print("Number of objects created:", Counter.count)

#Create a class Company with a class variable company_name.
#Implement a static method to validate email format.

import re
class Company:
    company_name = "Tech Solutions"   # class variable
    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return "Valid Email"
        else:
            return "Invalid Email"
# Example usage
print("Company:", Company.company_name)
print(Company.validate_email("teja@gmail.com"))
print(Company.validate_email("tejagmail.com"))

#INHERITANCE
#Create a base class Vehicle and derived class Bike
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Vehicle is starting")
class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   # call base class constructor
        self.model = model
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
# Example usage
b1 = Bike("Honda", "Shine")
b1.start()
b1.show_details()

#Create Person → Employee → Manager (multilevel inheritance).
#Override a method in child class and call parent method using super().
class Person:
    def show_role(self):
        print("I am a Person")
class Employee(Person):
    def show_role(self):
        print("I am an Employee")
        super().show_role()   # call parent method
class Manager(Employee):
    def show_role(self):
        print("I am a Manager")
        super().show_role()   # call parent method
# Example usage
m1 = Manager()
m1.show_role()

#Create a class BankAccount with private balance.
#Use getter and setter methods to update balance safely.
#Prevent negative salary using property decorators.

class BankAccount:
    def __init__(self, balance):
        self.__balance = 0
        self.balance = balance
    #SETTER
    @property
    def balance(self):
        return self.__balance

    #SETTER
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
acc = BankAccount(5000)
print("current balance:", acc.balance)
acc.balance = 7000
print("updated balance:", acc.balance)
acc.balance = -3000
print("final balance:", acc.balance)


#class with method area().Implement Circle and Rectangle.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print("Area:", shape.area())


#Demonstrate method overloading using default arguments.
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
# Example usage
calc = Calculator()
print(calc.add(2))          # one argument
print(calc.add(3, 6))      # two arguments
print(calc.add(3, 15, 20))  # three arguments

#Demonstrate operator overloading (__add__).
class Number:
    def __init__(self, value):
        self.value = value

    # Operator overloading for +
    def __add__(self, other):
        return Number(self.value + other.value)
# Example usage
n1 = Number(10)
n2 = Number(20)
result = n1 + n2   # calls __add__()
print("Result:", result.value)


#Create Engine class and use it inside Car class.
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(self.engine_type, "engine started")


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine   # Engine object used inside Car
    def start_car(self):
        print(self.brand, "car is starting...")
        self.engine.start()
# Example usage
eng = Engine("Petrol")
car1 = Car("Toyota", eng)
car1.start_car()

#Create Team class that contains multiple Player objects.
class Player:
    def __init__(self, name):
        self.name = name
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []   # list to store Player objects
    def add_player(self, player):
        self.players.append(player)
    def show_players(self):
        print("Team:", self.team_name)
        for player in self.players:
            print(player.name)
# Example usage
p1 = Player("Rohit")
p2 = Player("Virat")
p3 = Player("Gill")
team = Team("India")
team.add_player(p1)
team.add_player(p2)
team.add_player(p3)
team.show_players()
