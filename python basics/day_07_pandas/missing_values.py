"""Question: Fill missing numeric values with their column medians, replace missing text with "Unknown", drop rows with missing IDs, and verify the remaining missing-value counts."""

import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, None, 4, 5],
    "name": ["Aarav", None, "Rahul", "Meera", None],
    "age": [25, None, 29, 28, 35],
    "salary": [45000, 60000, None, 50000, 80000],
    "department": ["Engineering", "HR", None, "Marketing", "Engineering"]
})

print(df)

print(df.info())

print("\nMissing values in the DataFrame:")
print(df.isnull())

print("\nMissing values count for each column:")
print(df.isnull().sum())

print("\nDataFrame after dropping rows with missing IDs:")
df = df.dropna(subset=['id'])
print(df)

print("\nFilling missing numeric values with their column medians:")
df['age']=df['age'].fillna(df['age'].median())
print(df)

print("\nFilling missing text values with 'Unknown':")
df['name'] = df['name'].fillna("Unknown")
print(df)

print("\nFinal missing values count for each column:")
print(df.isnull().sum())