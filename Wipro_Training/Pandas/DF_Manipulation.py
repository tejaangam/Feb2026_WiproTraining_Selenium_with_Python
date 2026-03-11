'''

Creating data

Selecting data

Filtering data

Cleaning data

Transforming columns

Aggregating data

Merging datasets

Exporting results
'''
import numpy as np
#Creating data DFR using the dictionary
import pandas as pd

data = {
    "Name": ["Ram", "Sam", "John", "Priya"],
    "Age": [25,30,35,24],
    "Salary": [40000, 50000, 45000, 35000]
}
df = pd.DataFrame(data)
print(df)

#Selecting single data
print(df["Age"])

#Select multiple data or columns
print(df[["Age", "Name"]])

#Select rows using iloc-  (n-1)th or loc nth
print(df.loc[0:2])
print(df.iloc[0:1])

#filtering based on the conditions
df = pd.DataFrame(data)
print(df)

#employees  with salary > 40000
filtered  = df[df["Salary"] > 40000]
print(filtered)
#Multiple conditions
filtered1 = df[(df["Salary"] > 40000) & (df["Age"] > 25)]
print(filtered1)

#Cleaning the data - adding or modifying the columns
data= {
        "Name": ["Ram", "Sam", "John", "Priya"],
        "Salary": [40000, 50000, 45000, 35000]
    }
df = pd.DataFrame(data)
#add the column
df["Bonus"] = df["Salary"]*0.10
print(df)

#modify the current column
df["Salary"] =  df["Salary"] + 2000
print(df)

#sorting Data ascending and descending order

data = {
    "Name": ["Ram", "Sam", "John", "Priya"],
    "Age": [25,30,35,24],
    "Salary": [40000, 50000, 45000, 35000]
}
df = pd.DataFrame(data)

#Sort the salary in ascending order
sorted_df = df.sort_values("Salary", ascending = False)
print(sorted_df)

#handling missing value
#Replace all missing values in the dataframe (NaN)

data = {
    "Name": ["Ram", "Sam", None],
    "Age": [25, np.nan, 30]
}
df= pd.DataFrame(data)
print("missing ")
print(df.isnull())

#Replace all missing values Nan, None, NaT
df_filled = df.fillna(0)
print(df_filled)


data = {"Age": [25,None,30],
    "Salary": [40000, 50000, None]
        }
df =pd.DataFrame(data)
print(df)

df = df.fillna(0)
print(df)