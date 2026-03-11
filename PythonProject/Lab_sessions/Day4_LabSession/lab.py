#Create a class Book with attributes title and author.
#Create 3 different book objects and print all details

#Create a class Rectangle with a constructor that takes length and width and stores area and perimeter as object attributes.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
    def perimeter(self):
        print(2 * (self.length + self.width))
r = Rectangle(5, 3)
r.area()   
r.perimeter()
