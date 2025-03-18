import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
data = pd.read_csv("../output/final_cleaned_data.csv")

# Heatmap of Unemployment Rate by State
plt.figure(figsize=(10, 6))
heatmap_data = data.pivot_table(values='Unemployment Rate', index='Region', columns='Date')
sns.heatmap(heatmap_data, cmap='YlGnBu', linewidths=0.5)
plt.title('Unemployment Rate Heatmap by Region')
plt.savefig("../output/heatmap_unemployment.png")
plt.show()

# COVID-19 Impact Analysis
covid_data = data[(data['Date'] >= '2020-03-01') & (data['Date'] <= '2021-12-31')]
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Unemployment Rate', data=covid_data, color='red', label='COVID-19 Impact')
plt.title('Unemployment Rate During COVID-19 Period')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.savefig("../output/covid19_impact.png")
plt.show()
