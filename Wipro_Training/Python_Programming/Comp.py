#Comprehensions

#Lists
sqs = [x ** 2 for x in range (1,6)] 
print(sqs)

#with condition

evennumbers = [x for x in range(10) if x % 2 == 0]
print(evennumbers)

#dict comprehensions

salary = {"A": 50000, "B": 60000, "C": 70000}
updated_sal = {k: v + 0.1 * v for k, v in salary.items()}
print(updated_sal)

#filtering of dict

employees = {
    "HARSHA" : "ACTIVE",
    "TEJA"   : "ACTIVE",
    "BOBBY"  : "INACTIVE"
}

active_emp = {k : v for k, v in employees.items() if v == "ACTIVE"}
print(active_emp)

#set comprehensions

sqs = {x ** 2 for x in range(1,6)}
print(sqs)

#with condition

evennumbers = {x for x in range(10) if x % 2 == 0}
print(evennumbers)