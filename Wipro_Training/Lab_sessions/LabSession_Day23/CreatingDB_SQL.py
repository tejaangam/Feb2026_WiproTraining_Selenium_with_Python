import mysql.connector

# 1. CONNECT TO MYSQL SERVER
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tejaangam@1516"
)
cursor = connection.cursor()
# 2. CREATING  DATABASE
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")
# 3. CREATING TABLE
create_table_query = """
CREATE TABLE IF NOT EXISTS student_performance (
    StudentID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Math INT,
    Science INT,
    English INT,
    Attendance INT
)
"""
cursor.execute(create_table_query)
# 4. INSERTING DATA
insert_query = """
INSERT INTO student_performance 
(StudentID, Gender, Math, Science, English, Attendance)
VALUES (%s, %s, %s, %s, %s, %s)
"""
students = [
    (1,'Male',78,72,75,90),
    (2,'Female',65,70,68,85),
    (3,'Male',45,50,48,70),
    (4,'Female',32,30,35,60),
    (5,'Male',88,85,90,95),
    (6,'Female',54,60,57,80),
    (7,'Male',23,25,20,50),
    (8,'Female',76,80,74,88),
    (9,'Male',90,92,88,97),
    (10,'Female',40,42,38,65)
]

cursor.executemany(insert_query, students)
connection.commit()
print("Database, Table, and Data Created Successfully!")

# 5. VERIFYING DATA
cursor.execute("SELECT * FROM student_performance")
for row in cursor.fetchall():
    print(row)
cursor.close()
connection.close()