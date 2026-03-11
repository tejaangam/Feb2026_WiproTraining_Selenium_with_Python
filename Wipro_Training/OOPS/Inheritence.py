#SINGLE INHERITENCE
#parent ----> chiled class - properties from parent class are inherited by child class
#create the object of the child classes to bring inhertance in picture

class Employee:
    def __init__(self, name, empID):
        self.name = name
        self.empID = empID

    def emp_details(self):
        print(self.name, self.empID)
        print("Leave Request")
class Manager(Employee):
    def approve_leave(self):
        print("Leave Approved")

m = Manager(name="Teja", empID= 101)
m.emp_details() #from parent class
m.approve_leave() #from child class