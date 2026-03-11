#Write a Python function to sum all the numbers in a list.

def sumofList(numbers):
    total = 0
    for num in numbers:
        total  = total + num
    return total

numbers = [1, 2, 3, 4, 5]
result = sumofList(numbers)
print(result)

#Write a Python function to find the maximum of three numbers.

def maxofthree(a,b, c):
    if a >= b and a >= c:
        return a
    elif  b >= a and b >= c:
        return b
    else:
        return c

a = 10
b = 20
c = 30
result = maxofthree(a,b,c)
print(result)


