import sqlite3
import pandas as pd

# Load cleaned CSV
df = pd.read_csv(r"C:\Users\vijay\Desktop\Projects\Health_proj\data\healthcare_cleaned.csv")

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect(r"C:\Users\vijay\Desktop\Projects\Health_proj\data\healthcare.db")
cursor = conn.cursor()

# Save DataFrame as a table
df.to_sql('claims', conn, if_exists='replace', index=False)

# Example query: average billing per medical condition
query = "SELECT medical_condition, AVG(billing_amount) as avg_billing FROM claims GROUP BY medical_condition;"
result = pd.read_sql(query, conn)
print(result)

# Close the connection
conn.close()
