
# 1.Basic iterator that prints 1 to 5
print("Numbers from 1 to 5:")
def onetofive():
	for i in range(1, 6):
		yield i

# Usage
for i in onetofive():
	print(i)

# 2.Iterator class that returns next even number
print("Even numbers:")
class EvenNumberIterator:
	def __init__(self):
		self.current = 0

	def __iter__(self):
		return self

	def __next__(self):
		self.current += 2
		return self.current

# Example usage: print first 5 even numbers
even_iter = EvenNumberIterator()
for _ in range(5):
	print(next(even_iter))

# 3.explain and demonstrate the use of iter() and next().
print("Demonstrating iter() and next():")   
class EvenNumberIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        # Returns the iterator object itself
        return self

    def __next__(self):
        # Returns the next even number
        self.current += 2
        return self.current

# Demonstration
even_iter = EvenNumberIterator()
iterator = iter(even_iter)  # Calls __iter__()
print(next(iterator))       # Calls __next__(), prints 2
print(next(iterator))       # Calls __next__(), prints 4
print(next(iterator))       # Calls __next__(), prints 6

# 4. Generator to generate numbers from 1 to N
print("Numbers from 1 to N:")
def numbers_to_n(n):
	for i in range(1, n+1):
		yield i

# Usage example
for num in numbers_to_n(10):
	print(num)
	
#5 Write a generator to generate even numbers only.
print("Even numbers from 1 to 20:")
def evennums(n):
    if n % 2 == 0:
        yield n 
# Usage example
for num in range(1, 20):
    for even in evennums(num):
        print(even) 

#6.Write a generator to read a file line by line.
print("Reading file line by line:")
def readfile(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()  # Yield each line without leading/trailing whitespace
# Usage example
for line in readfile('example.txt'):
    print(line) 

#7.Create a generator for Fibonacci series.
print("Fibonacci series:")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
# Usage example: print first 10 Fibonacci numbers
for num in fibonacci(10):   
    print(num)  

