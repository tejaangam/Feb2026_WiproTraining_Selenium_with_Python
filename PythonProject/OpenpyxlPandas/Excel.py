import pandas as pd

df = pd.read_excel("C:/Users/hp/Wipro_Training/OpenpyxlPandas/students.xlsx", engine="openpyxl")
print(df)

data = {
    "Name": ["Ram", "Ravi", "Sita"],
    "Age": [20,21,19],
    "Marks":[85,90,86]
}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False, engine = "openpyxl")

df = pd.read_excel("output.xlsx", usecols=["Name"], engine="openpyxl")
print(df)

#Read all sheets
df = pd.read_excel("students.xlsx", sheet_name=None)
print(df)
#writing Multiple sheets
data1 = {
    "Product":["Laptop", "Phone"],
    "Sales":[10,20]
}

data2 = {
    "City": ["Delhi","Mumbai"],
    "Customers": [200,150]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

with pd.ExcelWriter("report.xlsx", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Sales")
    df2.to_excel(writer, sheet_name="Customers")