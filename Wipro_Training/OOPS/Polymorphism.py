#Polymorphism means taking many forms
# same method or function name will behave differently depending on the
#object type
#input arguments
#class implementation

#object type
print(len("python")) #string
print (len([1, 2, 3])) #list
print (len({1, 2, 3})) #tuple

#input arguments no of arguments / data types

class calculator:
    def add(self, a, b = 0, c = 0):
        return a + b + c
c = calculator()
print(c.add(5))
print(c.add(2,5))
print(c.add(10, 20, 30))

class Animal:
    def sound(self):
        print("animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Dog()
a.sound()