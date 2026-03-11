# Variables = used to store the data
#instance   variable = used to store the data of the object at class level
#local variable = inside the method only

class Student:

    #class variables
    school = "St Joseph Convent"

    def __init__(self, name, marks):
        self.name = name #instance vaiable or global variable
        self.marks = marks  #instance vaiable or global variable

    def show(self):
        city = "Hyderbad" #local variable
        print(self.name, self.marks)
        print(city)
        print(self.school)

s1= Student("Teja", 95)
s2 = Student("Ravi", 85)

s1.show()
s2.show()
