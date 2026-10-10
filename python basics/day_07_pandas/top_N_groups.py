"""Question: For each region, find the top three products by total revenue, grouping multiple sales of the same product before ranking."""

import pandas as pd

df = pd.DataFrame({
    "region": ["West", "West", "West", "West", "East", "East", "East", "East", "North", "North"],
    "product": ["Laptop", "Phone", "Mouse", "Laptop", "Phone", "Laptop", "Mouse", "Phone", "Laptop", "Keyboard"],
    "revenue": [50000, 20000, 5000, 30000, 25000, 40000, 3000, 10000, 45000, 7000]
})

# Step 1: Group by region and product, and calculate total revenue
df_summary = df.groupby(['region','product'])['revenue'].agg('sum').reset_index()

# Step 2: Get the top 3 products within each region
df_top3 = (
    df_summary.sort_values(["region", "revenue"], ascending=[True, False])
    .groupby("region")
    .head(3)
)
print(df_top3)