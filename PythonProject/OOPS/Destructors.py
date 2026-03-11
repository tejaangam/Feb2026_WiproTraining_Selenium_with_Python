#Destructors - when we want to destroy the object
# post conditions - cloisng of the browser , db coonectinon closing , reasing of certian resources
# clean up operations
# for  proper memory usage destcrutors should  be used
#  when db connection has to be closed -
# free the memory (garbage collection) which is automatically called
#Destructor runs when program ends or object is garbage-collected.
 

class Desct:
    def __init__(self):
        print("object created")
    
    def __del__(self):
        print("Closing the db connection")
a = Desct()
print("End of the program")
del a

class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print("File is opened")

    def readfile(self, filename):
        print("Reading the file")

    def __del__(self):
        print("Closing the file")
    
f = FileHandler("sample.txt")
f.readfile("sample.txt")
del f
