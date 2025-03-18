import pandas as pd

# Load the data
data = pd.read_csv("../output/cleaned_unemployment_data.csv")

# Handling missing values
data.dropna(inplace=True)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Correct any inconsistent data
data = data[data['Unemployment Rate'] > 0]

# Save cleaned data
data.to_csv("../output/final_cleaned_data.csv", index=False)
print("Data cleaning completed successfully!")
