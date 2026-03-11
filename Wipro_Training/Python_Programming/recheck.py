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
    obj.speak()  # Calls the speak method of the passed object
# Create instances of each class
dog = Dog() 
cat = Cat()
cow = Cow()
# Pass different objects to the same function
animal_sound(dog)  # Output: dog barks
animal_sound(cat)  # Output: cats meows
animal_sound(cow)  # Output: cows moos

#3.Multilevel Inheritance with Polymorphism
#Create Vehicle → Car → ElectricCar.
#Each class overrides the method fuel_type().
#Call the method using different object references.
class Vehicle:
    def fuel_type(self):
        return "Unknown fuel type"
class Car(Vehicle):
    def fuel_type(self):
        return "Petrol or Diesel"
class ElectricCar(Car):
    def fuel_type(self):
        return "Electricity"
# Create instances of each class
vehicle = Vehicle()
car = Car()
electric_car = ElectricCar()
# Call the method using different object references
print("Vehicle fuel type:", vehicle.fuel_type())  # Output: Vehicle fuel type: Unknown fuel type
print("Car fuel type:", car.fuel_type())          # Output: Car fuel type:
print("Electric Car fuel type:", electric_car.fuel_type())  # Output: Electric Car fuel type: Electricity

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
print("Is account1 balance greater than account2?", account1 > account2)  # Output: False

#2.Write a pattern to match a 10-digit mobile number.
