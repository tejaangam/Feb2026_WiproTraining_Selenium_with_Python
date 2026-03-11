from pymongo import MongoClient

# ===============================
# CONNECT TO MONGODB
# ===============================

client = MongoClient("mongodb://localhost:27017/")

# Create Database
db = client["sales_db"]

# Create Collection
collection = db["sales_data"]

# INSERT SALES DATA
sales_records = [
    {"OrderID":1001,"Date":"2025-01-05","Region":"East","Product":"Laptop","Category":"Electronics","Quantity":2,"Price":50000},
    {"OrderID":1002,"Date":"2025-01-12","Region":"West","Product":"Phone","Category":"Electronics","Quantity":3,"Price":20000},
    {"OrderID":1003,"Date":"2025-02-03","Region":"North","Product":"Tablet","Category":"Electronics","Quantity":1,"Price":30000},
    {"OrderID":1004,"Date":"2025-02-18","Region":"South","Product":"Monitor","Category":"Accessories","Quantity":4,"Price":15000},
    {"OrderID":1005,"Date":"2025-03-02","Region":"East","Product":"Laptop","Category":"Electronics","Quantity":3,"Price":50000},
    {"OrderID":1006,"Date":"2025-03-15","Region":"West","Product":"Phone","Category":"Electronics","Quantity":2,"Price":20000},
    {"OrderID":1007,"Date":"2025-04-01","Region":"North","Product":"Tablet","Category":"Electronics","Quantity":5,"Price":30000},
    {"OrderID":1008,"Date":"2025-04-12","Region":"South","Product":"Monitor","Category":"Accessories","Quantity":2,"Price":15000}
]
collection.insert_many(sales_records)
print("Sales data inserted")
client.close()