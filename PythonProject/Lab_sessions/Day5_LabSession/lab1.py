#1.Method Overriding with Inheritance
#Create a base class Employee with a method calculate_salary().
#Create a subclass Manager that overrides calculate_salary() and adds a bonus.
#Demonstrate runtime polymorphism using parent class reference.


class Employee:
    def calculate_salary(self, base_salary, bonus=0):
        return base_salary

class Manager(Employee):
    def calculate_salary(self, base_salary, bonus=0):
        return base_salary + bonus

# Demonstration of runtime polymorphism
manager = Manager()
print("Manager Salary:", manager.calculate_salary(50000, 10000))  # Output: Manager Salary: 60000

#2.Polymorphism Using Function Arguments
#Create classes Dog, Cat, and Cow each with a method speak().
#Write a function animal_sound(obj) that calls speak().
#Pass different objects to the same function.

class Dog:
    def speak(self):
        print("dog barks")
class Cat(Dog):
    def speak(self):
        print("cats meows")
class Cow(Dog):
    def speak(self):
        print("cows moos")
def animal_sound(obj):
    obj.speak()

d = Dog()
s = Cat()
c = Cow()

animal_sound(d)
animal_sound(s)
animal_sound(c)

#3.Multilevel Inheritance with Polymorphism
#Create Vehicle → Car → ElectricCar.
#Each class overrides the method fuel_type().
#Call the method using different object references.

class Vehicle:
    def fuel_type(self):
        print("Unkown Fuel Type")
class Car(Vehicle):
    def fuel_type(self):
        print("Petrol or Diesel")
class ElectricCar(Car):
    def fuel_type(self):
        print("Electricity")

vehicle = Vehicle()
car = Car()
electriccar = ElectricCar()

vehicle.fuel_type()
car.fuel_type()
electriccar.fuel_type()

#4.Operator Overloading
#Create a class BankAccount with attribute balance.
#Overload + to add balances and > to compare balances.
#Demonstrate polymorphic behavior of operators.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(self.balance + other.balance)
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        return NotImplemented
# Demonstration of operator overloading
account1 = BankAccount(1000)
account2 = BankAccount(2000)
# Adding two BankAccount instances
account3 = account1 + account2
print("Combined Balance:", account3.balance)  # Output: Combined Balance: 3000
# Comparing two BankAccount instances
print("Is account1 balance greater than account2?", account1 > account2)