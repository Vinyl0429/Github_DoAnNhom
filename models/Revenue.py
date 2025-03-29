import json
import math
import pandas as pd
from datetime import datetime
import os

# Load customer data
with open('../datasets/customers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.DataFrame(data)

# Parse datetime with multiple formats
def parse_datetime(x):
    formats = ["%d/%m/%Y %H:%M", "%H:%M %d/%m/%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(x, fmt)
        except ValueError:
            continue
    return None

# Apply datetime parsing
df['last_transaction_time'] = df['last_transaction_time'].apply(parse_datetime)
df.dropna(subset=['last_transaction_time'], inplace=True)

# Extract day, month, year
df['Day'] = df['last_transaction_time'].dt.day
df['Month'] = df['last_transaction_time'].dt.month
df['Year'] = df['last_transaction_time'].dt.year

# Create folder for Excel output
excel_folder = "../datasets"
os.makedirs(excel_folder, exist_ok=True)

# === REVENUE BY MONTH ===
df['Month/Year'] = df['last_transaction_time'].dt.strftime('%m/%Y')
monthly_revenue = df.groupby('Month/Year')['total_payment'].sum().reset_index()
monthly_revenue.columns = ['Month/Year', 'Total Revenue (VND)']

# Export monthly revenue to Excel
monthly_excel_path = os.path.join(excel_folder, "monthly_revenue.xlsx")
monthly_revenue.to_excel(monthly_excel_path, index=False)
print(f"✅ Exported file: {monthly_excel_path}")

# === REVENUE BY WEEK ===
df['Week'] = df['Day'].apply(lambda d: math.ceil(d / 7))
weekly_revenue = df.groupby(['Year', 'Month', 'Week'])['total_payment'].sum().reset_index()
weekly_revenue['Week/Month/Year'] = (
    'Week ' + weekly_revenue['Week'].astype(str) +
    ' - ' + weekly_revenue['Month'].astype(str).str.zfill(2) +
    '/' + weekly_revenue['Year'].astype(str)
)
weekly_revenue = weekly_revenue.sort_values(by=['Year', 'Month', 'Week'])
weekly_revenue = weekly_revenue[['Week/Month/Year', 'total_payment']]
weekly_revenue.columns = ['Week/Month/Year', 'Total Revenue (VND)']

# Export weekly revenue to Excel
weekly_excel_path = os.path.join(excel_folder, "weekly_revenue.xlsx")
weekly_revenue.to_excel(weekly_excel_path, index=False)
print(f"✅ Exported file: {weekly_excel_path}")