"""Question: Clean names by trimming whitespace and applying title case, extract email domains, and flag names containing "test" regardless of capitalization."""

import pandas as pd

df = pd.DataFrame({
    "name": ["  aNUSHA jAIN ", "DIYA SHAH", "test_user", "  dhyey patel", "TEST ACCOUNT "],
    "email": ["aarav@gmail.com", "diya@yahoo.com", "test@company.com",
              "rahul@outlook.com", "account@company.com"]
})

def clean_names(name):
    clean_text = " ".join(name.split())
    return clean_text.title()

def extract_email_domains(email):
    parts=email.split('@')
    return parts[-1]

def flag_names(name):
    name=name.lower()
    return "test" in name

df['name'] = df['name'].apply(clean_names)
df['domain'] = df['email'].apply(extract_email_domains)
df['flag'] = df['name'].apply(flag_names)
print(df)

