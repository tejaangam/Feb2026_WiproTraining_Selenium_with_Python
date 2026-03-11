Class = {
    1:"Teja",
    2:"Sharukh",
    3:"bunny"
}
#printing
print(Class)

#accesing the key which exists
print(Class[1])

#accesing the key which doesnot exists
print([4])

#Update the value of an existing key in a dictionary.
Class.update({"1":"Rahul"})
print(Class)   

#Delete a key from a dictionary using:
# using del

# using pop()
Class.pop(3)
print(Class)

#Find the number of key–value pairs in a dictionary.
print("length:")
print(len(Class))

#print only:keys, values, key–value pairs
Roll = Class.keys()
print(Roll)

Name = Class.values()
print(Name)



