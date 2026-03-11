try:
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("please enter valid number")


#generic exception
try:
    a = 10/0
except Exception as e:
    print(e)
else:
    print("Division successfull")
finally:
    print("Close the Browser")

#custom exception
age = int(input("enter the number"))
if age < 18:
    raise ValueError("Age must be 18 or above")