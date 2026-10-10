"""Question: Remove completely duplicated rows from a customer DataFrame, then keep only the most recent record for each customer based on the date column."""

import pandas as pd

df = pd.DataFrame({
    "customer_id": [101, 102, 101, 103, 102, 101],
    "name": ["Aarav", "Diya", "Aarav", "Rahul", "Diya", "Aarav"],
    "city": ["Ahmedabad", "Surat", "Ahmedabad", "Vadodara", "Surat", "Mumbai"],
    "date": ["2026-01-01", "2026-01-05", "2026-02-01",
             "2026-01-10", "2026-02-05", "2026-03-01"]
})

print("Original DataFrame:")
print(df)

print("\nDataFrame after removing completely duplicated rows:")
df= df.drop_duplicates()
print(df)

print("\nDataFrame after keeping only the most recent record for each customer:")
df = df.sort_values('date')
print(df)

print("\nDataFrame after dropping duplicates based on customer_id and keeping the last occurrence:")
df = df.drop_duplicates(subset=['customer_id'], keep='last')
print(df)

print("\nSetting back index on DataFrame")
df = df.reset_index(drop=True)
print(df)