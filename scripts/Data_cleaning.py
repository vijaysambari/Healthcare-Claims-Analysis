import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\vijay\Desktop\Projects\Health_proj\archive\healthcare_dataset.csv")

# clean the column names strip() , lower() , replace(' ','_')
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

#Before: '2024-01-31' → a string (you can’t do math with it) ,After: 2024-01-31 00:00:00 → a datetime object 

df['date_of_admission'] = pd.to_datetime(df['date_of_admission'])
df['discharge_date'] = pd.to_datetime(df['discharge_date'])


#Removes rows where the billing amount is less than or equal to 0. 
df = df[df['billing_amount'] > 0]

#Add new column: Length of stay
df['length_of_stay'] = (df['discharge_date'] - df['date_of_admission']).dt.days

#Create a fraud flag
df['fraud_flag'] = np.where((df['billing_amount'] > 40000) & (df['length_of_stay'] > 10), 1, 0)

print(df.columns)

df.to_csv(r"C:\Users\vijay\Desktop\Projects\Health_proj\data\healthcare_cleaned.csv", index=False)


