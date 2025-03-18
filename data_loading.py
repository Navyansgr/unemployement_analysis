import pandas as pd

# Load the dataset
file_path = "../data/unemployment_data.csv"
data = pd.read_csv(file_path)

# Display basic details
print("Dataset Overview:\n", data.info())
print("\nFirst 5 Rows:\n", data.head())

# Save the cleaned dataset
data.to_csv("../output/cleaned_unemployment_data.csv", index=False)
