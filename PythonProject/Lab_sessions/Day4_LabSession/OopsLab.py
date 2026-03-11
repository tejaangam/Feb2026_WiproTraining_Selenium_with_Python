# 1.Create a class Book with attributes title and author.Create 3 different book objects and print all details.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(self.title, self.author)


b1 = Book("Harry Potter:", "J.K. Rowling")
b2 = Book("Rich Dad Poor Dad:", "Robert Kiyosaki")
b3 = Book("The Odyssey:", "Homer")


b1.display()
b2.display()
b3.display()

