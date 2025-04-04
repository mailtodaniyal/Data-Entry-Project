import pandas as pd
import re

file_path = "customer_data.csv"  
df = pd.read_csv(file_path)

df = df.drop_duplicates()

df['Email'].fillna('unknown@example.com', inplace=True)
df['Phone'].fillna('Not Provided', inplace=True)
df['Name'].fillna('Unknown', inplace=True)

df['Email'] = df['Email'].str.lower()
df['Name'] = df['Name'].str.title()  

df['Phone'] = df['Phone'].astype(str).apply(lambda x: re.sub(r'\D', '', x) if x != 'Not Provided' else x)

valid_email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
df = df[df['Email'].str.match(valid_email_pattern, na=False)]

output_file = "cleaned_customer_data.csv"
df.to_csv(output_file, index=False)

print(f"Data cleaning completed! Cleaned file saved as: {output_file}")
