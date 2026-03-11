#Class is a blue print or template
#which describes the behavior and state of an object
#Data is put in variable
#Behavior is put in function


class Student:
    #Data or properties
    stu_name = "Teja"
    stu_ID = 45

    #self is ised to accecs the attributes of the class
    #it is automatically loaded
    #self represents the current instance of the class

#create a function to access the data
    def dispalyStuDetails(self):
        print(f"The name of the student is: {self.stu_name}")
        print(f"The ID of the student is: {self.stu_ID}")

#create an object of the class
s = Student()
s.dispalyStuDetails()

#write a program to create a class for an employee - with data - emp id , emp name , emp  dept and create function to display the data with 2 objects 
 
class Employee:
    emp_ID = 101
    emp_name = "Teja"
    emp_Dept = "Developer"

def displayEmpDetails(self):
    print(self.emp_ID)
    print(self.emp_name)
    print(self.emp_Dept)

e =Employee()
displayEmpDetails(e)


