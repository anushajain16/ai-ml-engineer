"""Question: Merge orders with customer details, identify orders with missing customer records, and find customers who have never placed an order."""

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "customer_id": [101, 102, 105, 101, 104]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "name": ["Aarav", "Diya", "Rahul", "Meera"],
    "city": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]
})

# 1. Merge orders with customer details
merged = orders.merge(
    customers,
    on="customer_id",
    how="left",
)

print("Merged orders:")
print(merged)

# 2. Find orders with missing customer records
missing_customers = merged[merged['name'].isnull()]

print("\nOrders with missing customer records:")
print(missing_customers[["order_id", "customer_id"]])

# 3. Find customers who never placed an order
customers_without_orders = customers[
    ~customers["customer_id"].isin(orders["customer_id"])
]

print("\nCustomers who never placed an order:")
print(customers_without_orders)