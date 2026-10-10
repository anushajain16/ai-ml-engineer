"""Question: Using a DataFrame, select the same three rows and two columns using loc and iloc, then set a column as the index and repeat the selection."""

import pandas as pd

df = pd.DataFrame({
    "id": [101, 102, 103, 104, 105],
    "name": ["Aarav", "Diya", "Rahul", "Meera", "Kabir"],
    "age": [25, 30, 29, 28, 35],
    "salary": [45000, 60000, 75000, 50000, 80000]
}, index = [1,2,3,4,5])

data = df.loc[1:3,['name','age']]
print("Selected rows and columns using loc:")
print(data)

data1 = df.iloc[[0, 1, 2], [1, 2]]
print("\nSelected rows and columns using iloc:")
print(data1)
