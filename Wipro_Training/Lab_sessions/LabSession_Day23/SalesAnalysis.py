from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt


# CONNECT TO MONGODB
client = MongoClient("mongodb://localhost:27017/")
db = client["sales_db"]
collection = db["sales_data"]

# LOAD DATA INTO PANDAS
data = list(collection.find({}, {"_id":0}))
df = pd.DataFrame(data)

print("Data Loaded:")
print(df.head())

# FEATURE ENGINEERING
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]

# ANALYSIS
# Revenue by Region
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
print(region_revenue)

# Monthly Revenue Trend
df["Month"] = df["Date"].dt.to_period("M")
monthly_revenue = df.groupby("Month")["Revenue"].sum()

# Top 5 Products
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)

# Category Contribution
category_revenue = df.groupby("Category")["Revenue"].sum()

# VISUALIZATIONS
# Bar Chart → Revenue by Region
plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.show()

# Line Plot → Monthly Revenue Trend
plt.figure()
monthly_revenue.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Pie Chart → Category Contribution
plt.figure()
category_revenue.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Contribution")
plt.ylabel("")
plt.show()

# Horizontal Bar → Top Products
plt.figure()
top_products.plot(kind="barh")
plt.title("Top Products by Revenue")
plt.xlabel("Revenue")
plt.show()

client.close()