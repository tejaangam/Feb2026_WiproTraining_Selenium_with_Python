import mysql.connector

print("Before connection")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tejaangam@1516"
)

print("Connected successfully")

conn.close()
print("Closed")