
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load cleaned data ---
df = pd.read_csv(r"C:\Users\vijay\Desktop\Projects\Health_proj\data\healthcare_cleaned.csv")

# --- Basic overview ---
print("Dataset info:")
print(df.info())
print("\nDataset description:")
print(df.describe(include='all'))

# --- Distribution of billing amount ---
plt.figure(figsize=(10,4))
sns.histplot(df['billing_amount'], bins=40, kde=True, color='skyblue')
plt.title("Distribution of Billing Amount")
plt.xlabel("Billing Amount")
plt.ylabel("Frequency")
plt.show()

# --- Average billing by medical condition ---
avg_billing = df.groupby('medical_condition')['billing_amount'].mean().sort_values(ascending=False)
print("\nAverage Billing Amount by Medical Condition:")
print(avg_billing)

plt.figure(figsize=(12,5))
sns.barplot(x=avg_billing.index, y=avg_billing.values, palette='viridis')
plt.xticks(rotation=45)
plt.ylabel("Average Billing Amount")
plt.title("Average Billing by Medical Condition")
plt.show()

# --- Admissions by type ---
admission_counts = df['admission_type'].value_counts()
print("\nAdmissions by Type:")
print(admission_counts)

plt.figure(figsize=(6,4))
sns.barplot(x=admission_counts.index, y=admission_counts.values, palette='Set2')
plt.title("Admissions by Type")
plt.ylabel("Number of Admissions")
plt.show()

# --- Relationship between Length of Stay and Billing Amount ---
plt.figure(figsize=(8,5))
sns.scatterplot(x='length_of_stay', y='billing_amount', data=df, hue='fraud_flag', alpha=0.6)
plt.title("Billing Amount vs Length of Stay (Fraud Flag Highlighted)")
plt.xlabel("Length of Stay (days)")
plt.ylabel("Billing Amount")
plt.show()

# --- Fraud flag summary ---
fraud_summary = df['fraud_flag'].value_counts(normalize=True) * 100
print("\nFraud Flag Summary (% of Claims):")
print(fraud_summary)
