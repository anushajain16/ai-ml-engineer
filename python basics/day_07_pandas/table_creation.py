"""Question: Load a CSV file into a DataFrame and display its dimensions, column data types, missing-value counts, and descriptive statistics for numeric columns."""

import pandas as pd 

data = pd.read_csv('employees.csv')
print(data)

dimension = data.ndim
print("\nDimension of data: ", dimension)

dimensions = data.shape
print("\nDimensions of csv data: ", dimensions)

data_type = data.dtypes
print("\nData types for each column: ", data_type)

missing_values = pd.isnull(data).sum()
print("\nNull values in the data",missing_values)

statistical_summary = data.describe()
print("\nStatistical summary of the data \n",statistical_summary)