"""Question: Convert an order-date column to datetime, extract year, month and weekday, count orders per month, and calculate the days between each order date and today."""

import pandas as pd

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "order_date": ["2026-01-15", "2026-02-20", "2026-02-25", "2026-03-10", "2026-03-15"]
})

# 1. Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# 2. Extract year, month, and weekday
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["weekday"] = df["order_date"].dt.day_name()

# 3. Count orders per month
monthly_orders = df.groupby(
    ["year", "month"]
)["order_id"].count()

# 4. Calculate days between each order date and today
today = pd.Timestamp.today().normalize()
df["days_since_order"] = (today - df["order_date"]).dt.days

print("Updated DataFrame:")
print(df)

print("\nOrders per month:")
print(monthly_orders)
