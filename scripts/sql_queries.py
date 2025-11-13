# sql_queries.py
import pandas as pd
import sqlite3
import os

# --- Paths ---
cleaned_csv_path = r"C:\Users\vijay\Desktop\Projects\Health_proj\data\healthcare_cleaned.csv"
kpi_csv_path = r"C:\Users\vijay\Desktop\Projects\Health_proj\data\kpi_summary.csv"
db_path = r"C:\Users\vijay\Desktop\Projects\Health_proj\data\healthcare.db"

# --- Load cleaned data ---
df = pd.read_csv(cleaned_csv_path)

# --- Optional: save to SQLite database ---
os.makedirs(os.path.dirname(db_path), exist_ok=True)
conn = sqlite3.connect(db_path)
df.to_sql('claims', conn, if_exists='replace', index=False)

# --- KPI Calculations ---

# 1️⃣ Total number of claims
total_claims = df.shape[0]

# 2️⃣ Total billing amount
total_billing = df['billing_amount'].sum()

# 3️⃣ Average billing amount
avg_billing = df['billing_amount'].mean()

# 4️⃣ Admissions by type
admissions_by_type = df['admission_type'].value_counts()

# 5️⃣ Average length of stay
avg_length_of_stay = df['length_of_stay'].mean()

# 6️⃣ Fraudulent claims percentage
fraud_percentage = df['fraud_flag'].mean() * 100

# 7️⃣ Top 10 medical conditions by total billing
top_conditions = df.groupby('medical_condition')['billing_amount'].sum().sort_values(ascending=False).head(10)

# 8️⃣ Top 10 doctors by number of claims
top_doctors = df['doctor'].value_counts().head(10)

# --- Print KPIs ---
print("=== Key Performance Indicators (KPIs) ===")
print(f"Total Claims: {total_claims}")
print(f"Total Billing Amount: ${total_billing:,.2f}")
print(f"Average Billing Amount: ${avg_billing:,.2f}")
print(f"Average Length of Stay: {avg_length_of_stay:.2f} days")
print(f"Fraudulent Claims (%): {fraud_percentage:.2f}%\n")

print("Admissions by Type:")
print(admissions_by_type, "\n")

print("Top 10 Medical Conditions by Total Billing:")
print(top_conditions, "\n")

print("Top 10 Doctors by Number of Claims:")
print(top_doctors, "\n")

# --- Save KPI summary CSV (optional for Power BI) ---
kpi_summary = pd.DataFrame({
    'KPI': ['Total Claims', 'Total Billing Amount', 'Average Billing Amount', 
            'Average Length of Stay', 'Fraudulent Claims (%)'],
    'Value': [total_claims, total_billing, avg_billing, avg_length_of_stay, fraud_percentage]
})

kpi_summary.to_csv(kpi_csv_path, index=False)
print(f"KPI summary saved to: {kpi_csv_path}")

# --- Close DB connection ---
conn.close()
