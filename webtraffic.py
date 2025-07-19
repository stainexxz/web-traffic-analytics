import pandas as pd

# Load the CSV file
df = pd.read_csv("C:\\Users\\melvi\\Documents\\Project Hub\\Project 2 {Web Traffic Analytics}\\website_traffic_dataset.csv")  # replace with the actual filename
# Simulating Timestamp column for time-based analytics
df['Timestamp'] = pd.date_range(start='2023-01-01', periods=len(df), freq='h')

# Check for missing values
df.isnull().sum()


df.drop_duplicates(inplace=True)
df.dtypes
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.columns.to_list()

df.head()
df.info()

print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.countplot(x='traffic_source', data=df)
plt.title('Traffic Source Distribution')
plt.yticks(rotation=45)
plt.xticks(rotation=45)
plt.xlabel('Traffic Source')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.yticks(rotation=45)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("finish")
