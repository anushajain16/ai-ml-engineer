"""Question: In a sales DataFrame, calculate total sales from price and quantity, classify sales as "high" or "low" based on whether total exceeds 1,000, and categorize customers into age groups."""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "product": ["Laptop", "Mouse", "Phone", "Keyboard", "Monitor"],
    "price": [50000, 500, 20000, 1500, 12000],
    "quantity": [2, 5, 1, 2, 3],
    "age": [17, 25, 40, 61, 35]
})

# 1. Calculate total sales for each product
df['sales'] = df['price']*df['quantity']

# 2. Classify sales as high or low
df['sales_category'] = np.where(
    df['sales'] > 1000, 'high', 'low'
)

# 3. Categorize customers into age groups
def categorize_age(age):
    if age < 18:
        return 'Under 18'
    elif age < 36:
        return '18-35'
    elif age < 60:
        return '36-59'
    else:
        return '60+'

df['age_group'] = df['age'].apply(categorize_age)
print(df)