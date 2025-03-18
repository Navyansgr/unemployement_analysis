import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
data = pd.read_csv("../output/final_cleaned_data.csv")

# Unemployment Trend over Time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Unemployment Rate', data=data, label='Unemployment Rate')
plt.title('Unemployment Rate Over Time in India')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.savefig("../output/unemployment_trends.png")
plt.show()

# Region-wise Unemployment Analysis
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Unemployment Rate', data=data)
plt.title('Unemployment Rate by Region')
plt.xticks(rotation=45)
plt.savefig("../output/region_unemployment.png")
plt.show()
