# Default methods --- built in methods, user defined methods - method name, method body

#parameterized methods 
#it allows the same method to behave differently for diff inputs

class Calculator:
    def add(self, a, b):
        print(a+b)


#Default Parameters
c = Calculator()
c.add(10, 20)
c.add(5, 4)

class Test:
    def run(self, browser = "Chrome"):
        print("Running on", browser)

t = Test()
t.run()
t.run("Edge")

# *args parameterized methods
