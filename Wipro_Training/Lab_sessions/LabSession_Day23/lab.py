# STEP 1: IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt

# STEP 2: LOAD CSV FILE
df = pd.read_csv("sales.csv")
print("First 5 Rows:")
print(df.head())

# STEP 3: DATA CLEANING
# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Check null values
print("\nNull Values:")
print(df.isnull().sum())

# Fill numeric null values (if any)
df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(0)
df["Revenue"] = df["Revenue"].fillna(0)

# Drop rows with missing critical fields
df = df.dropna(subset=["OrderID", "Date", "Region", "Product", "Category"])


# STEP 4: ANALYSIS
# 1. Revenue by Region
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
print(region_revenue)

# 2. Monthly Revenue Trend
df["Month"] = df["Date"].dt.to_period("M")
monthly_revenue = df.groupby("Month")["Revenue"].sum()
print("\nMonthly Revenue:")
print(monthly_revenue)

# 3. Best Performing Category
category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Category:")
print(category_revenue)

# 4. Top 5 Products
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:")
print(top_products)


# STEP 5: VISUALIZATIONS

# Bar Chart → Revenue by Region
plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.show()

# Line Plot → Monthly Revenue Trend
plt.figure()
monthly_revenue.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()

# Pie Chart → Category Contribution
plt.figure()
category_revenue.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Contribution")
plt.ylabel("")
plt.show()

# Horizontal Bar Chart → Top 5 Products
plt.figure()
top_products.plot(kind="barh")
plt.title("Top 5 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()