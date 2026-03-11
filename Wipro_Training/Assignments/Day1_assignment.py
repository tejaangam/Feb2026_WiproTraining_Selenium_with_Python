#1. Find the sum of numbers from 1 to 50 using xrange
#We use xrange() function only in python 2
'''
total = 0

for i in xrange(1, 51):
    total += i

print(total)
'''
#2. Count how many times "a" appears in a string using enumerate
text = "banana"
count = 0
for index, char in enumerate(text):
    if char == "a":
        count += 1
print("Count of a is:", count)


check_vowel = lambda s: s[0].lower() in "aeiou"

print(check_vowel("Apple"))   # True
print(check_vowel("banana"))  # False

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x * x, numbers))

print(squared)


class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        for i in range(2, self.limit + 1, 2):
            yield i
even = EvenNumbers(20)

for num in even:
    print(num)

def numbers():
    for i in range(1, 6):
        yield i

for num in numbers():
    print(num)


    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def display(self):
            print("Name:", self.name)
            print("Salary:", self.salary)


    class Manager(Employee):
        def __init__(self, name, salary, bonus):
            super().__init__(name, salary)
            self.bonus = bonus

        def display(self):
            super().display()
            print("Bonus:", self.bonus)


    # Example usage
    emp = Employee("Teju", 50000)
    emp.display()

    print()

    mgr = Manager("Rahul", 80000, 20000)
    mgr.display()


    class Grandparent:
        def __init__(self):
            self.family_name = "Sharma"
        def show_grandparent(self):
            print("Family Name:", self.family_name)
    class Parent(Grandparent):
        def __init__(self):
            super().__init__()
            self.house = "Own House"
        def show_parent(self):
            print("Property:", self.house)
    class Child(Parent):
        def __init__(self):
            super().__init__()
            self.name = "Rohit"
        def show_child(self):
            print("Child Name:", self.name)
    # Creating object of Child
    c = Child()
    c.show_grandparent()
    c.show_parent()
    c.show_child()