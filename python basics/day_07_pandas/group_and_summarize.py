"""Question: Calculate total and average revenue for each region and count the number of orders for every region-product combination."""

import pandas as pd

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "region": ["West", "East", "West", "North", "East", "West", "North", "East"],
    "product": ["Laptop", "Phone", "Phone", "Laptop", "Laptop", "Phone", "Phone", "Phone"],
    "revenue": [50000, 20000, 15000, 45000, 40000, 18000, 12000, 22000]
})

df_summary = df.groupby('region')['revenue'].agg(['mean','sum'])
print(df_summary)

order_counts = df.groupby(['region', 'product']).size()
print(order_counts)

