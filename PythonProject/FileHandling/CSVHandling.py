import csv


#Reading the csv file
with open("C:/Users/hp/Wipro_Training/DataFormat/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Writing the csv file 
with open("C:/Users/hp/Wipro_Training/DataFormat/write.csv", "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "marks"])
    writer.writerow(["1", "Teja", "95"])
    writer.writerow(["2", "Siva", "90"])

#appending the data to csv file
with open("C:/Users/hp/Wipro_Training/DataFormat/write.csv", "a" ,newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3, "Kiran", 88])