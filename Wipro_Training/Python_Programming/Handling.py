#write a program to handle invalid user input 
    try:
        number = int(input("enter a number"))
        print(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")