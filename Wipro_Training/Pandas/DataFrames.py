# DataFrame is a 2-Dimensional labeled data structure (rows-columns)
#like an Excel SQL tables

import pandas as pd

#Create DataFrame from list of dictionaries

data = [
    {"Name": "Ram", "Age": 25},
    {"Name": "Sam", "Age": 30},
    {"Name": "John", "Age": 27}
]

df = pd.DataFrame(data)
print(df)

# Create a DataFrame from Dictionary of series

s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])

df = pd.DataFrame({"A": s1, "B": s2})
print(df)

#Create DataFrame from numpy Array
import numpy as np
arr = np.array([[1,2], [3,4], [5,6]])
df = pd.DataFrame(arr, columns=["A", "B"])
print(df)

#create dataframe using csv file
df = pd.read_csv("employees.csv")
print(df)

#create empty df
df = pd.DataFrame()
print(df)

#create DataFrame with custom index
data = {
    "Name": ["Ram", "Sita"],
    "Age": [25, 30]
}
df = pd.DataFrame(data, index= ["emp1", "emp2"])
print(df)