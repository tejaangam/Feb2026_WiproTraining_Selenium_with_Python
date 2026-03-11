import mysql.connector

#create connection to my sql database
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tejaangam@1516",

)

#connection.cursor() is a method used in python database drivers(like sqlite3) psycopg2 mysql-connect
# to create a cursor object from an established database connection.

cursor = connection.cursor()
print("Connected Successfully")

#create database
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
connection.commit()

#Now reconnect with database:
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tejaangam@1516",
    database = "school"
)

cursor = connection.cursor()
print("Connected successfully")

#create table

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS students(
        studentid INT AUTO_INCREMENT PRIMARY KEY,
        studentname VARCHAR(50),
        subject VARCHAR(50),
        marks INT
        )
    ''')

connection.commit()
#Insert data
query = "INSERT INTO students (studentname, subject, marks) VALUES (%s, %s, %s)"
values = ("john", "Math", 85)

cursor.execute(query, values)
connection.commit()
# Insert multiple records
students_data = [
    ("Ravi", "Science", 90),
    ("Sneha", "Math", 78),
    ("Kiran", "Science", 88)
]
cursor.executemany(query, students_data)
connection.commit()
#read data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

# update the data
cursor.execute("UPDATE students SET marks=95 WHERE studentname='John'")
connection.commit()

# delete data
cursor.execute("DELETE FROM students WHERE studentname='Sneha'")
connection.commit()   #  added commit

# 🔹 close connection properly
cursor.close()
connection.close()

