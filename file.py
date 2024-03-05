import pandas as pd
from datetime import datetime

# Task 1: Load and Inspect the Data
df = pd.DataFrame(sales_data)

print("Task 1: Load and Inspect the Data")
print("Number of Transactions:", len(df))
print("Columns in DataFrame:", df.columns)
print("Sample of the Data:")
print(df.head())
print()

# Task 2: Data Cleaning
print("Task 2: Data Cleaning")
# Check for missing values
missing_values = df.isnull().any().any()

if missing_values:
    print("Missing Values Found. Handling Missing Values...")
    df = df.dropna()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print("Data Cleaning Complete")
print()

# Task 3: Data Analysis
print("Task 3: Data Analysis")
# Calculate total revenue for each product
total_revenue_per_product = df.groupby('Product')['Revenue'].sum()

# Determine the top-selling product based on the total number of units sold
top_selling_product = total_revenue_per_product.idxmax()

# Identify the month with the highest total revenue
df['Month'] = df['Date'].dt.strftime('%B %Y')
total_revenue_per_month = df.groupby('Month')['Revenue'].sum()

highest_revenue_month = total_revenue_per_month.idxmax()

print("Total Revenue per Product:")
print(total_revenue_per_product)
print("Top Selling Product:", top_selling_product)
print("Total Revenue per Month:")
print(total_revenue_per_month)
print("Month with the Highest Total Revenue:", highest_revenue_month)
print()

# Task 4: Data Visualization (Optional)
print("Task 4: Data Visualization (Optional)")
# Create a simple text-based visualization
print("Text-Based Visualization - Total Revenue per Product:")
print(total_revenue_per_product)
print()

# Bonus: Explore additional insights or analyses
# (For example, you could calculate average revenue per unit sold, perform statistical analyses, etc.)
