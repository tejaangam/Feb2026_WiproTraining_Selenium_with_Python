
#default function
def printdata():
    print("Hello World!!")

#call the function
printdata()

#functions with parameters
def printdata(name):
    print("Hello", name)

#pass the argument
printdata("Teja")
printdata("Sai")


#using return 
def sq(num):
    result = num*num
    return result

square = sq(3)
print("square: ", square)

#function pass

def func_pass():
    pass

#call the function
func_pass()

#function calling another function

def areaofrect(len, width):
    return len * width

def areaofSq(side):
    return side * side

value = areaofrect(4,5)
sq = areaofSq(value)
print(sq)
#multiple return values
def cal(a, b):
    return a+b, a-b, a*b
add, sub, mul = cal(10, 5)
print(add)
print(sub)
print(mul)


#function with loop
def even(limit):
    for i in range(2, limit+1, 2):
        print(i)
even(10)

#function with if-else

def even(limit):
    if limit % 2 == 0:
        return "even"
    else:
        return "odd"

print(even(10))
print(even(13))


