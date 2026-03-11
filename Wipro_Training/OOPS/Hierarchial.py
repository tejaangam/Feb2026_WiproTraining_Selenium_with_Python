#HIERARCHIAL INHERITANCE

class Employee:
    def login(self):
        print("Employee is logged in")

class Developer(Employee):
    def write_code(self):
        print("Deveeloper writes code")

class Tester(Employee):
    def test_app(self):
        print("Test the application")

dev = Developer() #from child 1
test = Tester()   #from child 2

Developer.login(dev) #from parent class
Developer.write_code(dev) #from child 1
Tester.test_app(test) #from child 2 
