"""Given an employee DataFrame, select only the name and salary columns, filter Engineering employees earning over 50,000, and return the five highest-paid employees."""

import pandas as pd

employee = pd.DataFrame({
    "name":["Anusha", "Hemlata", "Mukesh", "Abheek", "Dhyey"],
    "age" : [22,47,52,18,21],
    "salary" : [52000,20000,60000,15000,55000],
    "department" :["Engineering","HR","Business","Engineering","Engineering"]
})

new = employee[['name','salary']]
print("Selected columns:")
print(new)

filtered = employee[(employee['department'] == 'Engineering') & (employee['salary'] > 50000)].nlargest(5, 'salary')
print("\nFiltered employees:")
print(filtered)