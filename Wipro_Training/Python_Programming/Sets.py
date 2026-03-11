#sets do not allow duplicate elements
# unordered collection

# create a student_id set integer type
stu_id = {112, 113, 114, 115}
print(stu_id)

# create a string type set
letters = {'a', 'b', 'c', 'd', 'e'}
letter={'a', 'c', 'e'}
print(letters)

# create a mixed set
mixed_set = {"Hello", 1,-7,8,9}
print(mixed_set)

#create an empty set
empty_set = set()

# add elements to set
letters.add('f')
print(letters)

#copy
letters.copy()
print(letters)

#clear
letters.clear()
print(letters)

#difference
print(letters.difference(letter))

#difference update
print(letters.symmetric_difference_update(letter))

#discard
letters.discard('p')
print(letters)

#intersection
print(letters.intersection(letter))
#intersection_update
print(letters.intersection_update(letter))
#isdisjoint
print(letters.isdisjoint(letter))

print(letters.issubset(letter))

print(letters.issuperset(letter))

print(letters.union(letter))

print(letters.update(letter))

print(letters.pop())

print(letters.remove('c'))