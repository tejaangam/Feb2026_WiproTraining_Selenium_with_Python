import json

with open("C:/Users/hp/Wipro_Training/DataFormat/employee.json" , "r") as file:
    data = json.load(file)

# read the json file
print(data)
print(data["name"])

with open("C:/Users/hp/Wipro_Training/DataFormat/nested.json" , "r") as file:
    data = json.load(file)


email = data["user"]["profile"]["email"]
print(email)

#write the json file
with open("C:/Users/hp/Wipro_Training/DataFormat/nested.json", "w") as file:
    json.dump(data, file)

print(data)

#update or modify the value
## steps: 
 #1. Read the data
 #2. Modify or update the data 
 #3. Write the data 
{
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}

# ********* READ *************
with open("C:/Users/hp/Wipro_Training/DataFormat/writejson.json", "r") as file:
    data = json.load(file)
print  (data)

# ********* MODIFY *************
data ["name"] = "Teja"

# ********* WRITE *************
with open("C:/Users/hp/Wipro_Training/DataFormat/writejson.json", "w") as file:
    json.dump(data, file, indent = 4)


#File exception Handling
try:
    with open("C:/Users/hp/Wipro_Training/DataFormat/employee.json" , "r") as file:
        data = json.load(file)
    print(data)
except FileNotFoundError:
    print("File not found.")