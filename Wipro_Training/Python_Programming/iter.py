#iter() method - built in method
#create a iterator from a iterable

#iterations - looping in the collection of items

a=[10,20,30,40,50]

# convert the list into a iterator
iterator = iter(a)

# next() allow the user to access the elements
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# convert the string to a iterator

s="hello"
iterator = iter(s)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


#convert the dict to a iterator
d = {'a':1, 'b':2, 'c':3}
iterator = iter(d)
print(next(iterator))
print(next(iterator))


# for loop to iterate

for key in iterator:
    print(key)


d={'a':1, 'b':2, 'c':3}
for key, value in d.items():
    print(key,"->", value)

# iter(callable, sentinel)


def get_input():
    return input("Enter value:")
for value in iter(get_input, "quit"):
    print("You entered:", value)

print("Loop ended")