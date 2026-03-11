#RANGE FUNCTION: range() function returns an immutable sequence of numbers
#Range(stop); Range(start, stop); Range(start, stop, step)
#stop value excluded, default start = 0, default step = 1
#step can't be nagative, can't be zero
#range returns range object
#range supports indexing10

#Range Example:

def sum_n(n):
    for i in range(1):
        result = (n * (n + 1)) / 2
        print (result)
print(sum_n(5))

#ex2:
for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()

for i in range(3):
    for j in range(2):
        print(i,j)