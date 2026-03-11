# Pandas - high perfomance data manipulation and data analysis tool
# 2008 Mckinnley
# data frame object
# list , csv , josn , pdf

# series - A one-dimensional labeled homogeneous array, sizeimmutable.
# DataFrames    2  A two-dimensional labeled, size-mutable tabular structure with potentially heterogeneously typed columns.

import pandas as pd


#creation of series
data= ['Steve', '35', 'Male', '3.5']
series = pd.Series(data, index = ['Name', 'Age', 'Gender', 'Rating'])
print(series)

#create series from list
data = [100,200,300]
s = pd.Series(data, index=['a','b','c'])
print(s)

#create series from dictionary
data = {'a': 1, 'b': 2, 'c':3}
d = pd.Series(data)
print(d)

# create series numpy 
import numpy as np
arr = np.array([1,2,3,4])
s = pd.Series(arr)
print(s)

#create an empty series
s = pd.Series(dtype=float)
print(s)
