class Employee:
    
    def __init__(self, name, salary):

        self.name = name
        self.salary = salary    

    def display(self):
        print(self.name, self.salary)

e1 = Employee("teja" , 50000)
e2 = Employee("Bobby" , 60000)

e1.display()
e2.display()

#constructor overloading
class Numbers:
    def __init__(self, *args):
        self.values = args

n = Numbers(10, 20, 30, 40)
print(n.values)

m = Numbers(10, 20)
print(m.values)

p = Numbers(5)
print(p.values)

#Parent and child constructors
#super key word for constructors for accessing parent constructor 

class Parent:
    def __init__(self):
        print("I am the parent constructor")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child1 constructor")

c = Child1()

class Child2(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child2 constructor")

c = Child2()