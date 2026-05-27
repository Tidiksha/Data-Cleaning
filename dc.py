import pandas as pd

# Load dataset
df = pd.read_excel("sales_data.xlsx")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(0)

# Total Sales
total_sales = df['Sales'].sum()

# Total Profit
total_profit = df['Profit'].sum()

# Create summary report
summary = pd.DataFrame({
    'Total Sales': [total_sales],
    'Total Profit': [total_profit]
})

# Save cleaned data
df.to_excel("cleaned_sales_data.xlsx", index=False)

# Save summary
summary.to_excel("sales_summary.xlsx", index=False)

print("Data Cleaning and Reporting Completed")