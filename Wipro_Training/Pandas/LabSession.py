import pandas as pd
import numpy as np

# 1. Create DataFrame with missing values
data = {
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Kiran"],
    "Age": [25, None, 30, 28, None],
    "City": ["Bangalore", "Hyderabad", "Bangalore", "Chennai", "Bangalore"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, None, 55000, 70000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 2. Detect missing values
print("\nMissing Values (True = Missing):")
print(df.isnull())


# 3. Replace missing values with 0
df_filled = df.fillna(0)

print("\nAfter Replacing Missing Values with 0:")
print(df_filled)


# 4. Drop rows containing missing values
df_dropped = df.dropna()

print("\nAfter Dropping Rows with Missing Values:")
print(df_dropped)


# 5. Sort by Age (ascending)
df_sorted_age = df_filled.sort_values(by="Age", ascending=True)

print("\nSorted by Age (Ascending):")
print(df_sorted_age)


# 6. Sort by Salary (descending)
df_sorted_salary = df_filled.sort_values(by="Salary", ascending=False)

print("\nSorted by Salary (Descending):")
print(df_sorted_salary)


# 7. Groupby Department – Average Salary
avg_salary = df_filled.groupby("Department")["Salary"].mean()

print("\nAverage Salary per Department:")
print(avg_salary)


# 8. Groupby Department – Total Salary
total_salary = df_filled.groupby("Department")["Salary"].sum()

print("\nTotal Salary per Department:")
print(total_salary)


# 9. Filter employees where Age > 25 AND City = 'Bangalore'
filtered = df_filled[(df_filled["Age"] > 25) & (df_filled["City"] == "Bangalore")]

print("\nEmployees with Age > 25 and City = Bangalore:")
print(filtered)


# 10. Create new column 'Tax' (10% of Salary) using apply()
df_filled["Tax"] = df_filled["Salary"].apply(lambda x: x * 0.10)

print("\nDataFrame with Tax Column:")
print(df_filled)