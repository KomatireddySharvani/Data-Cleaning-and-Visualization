# Data Cleaning & Visualization using AirTravel Dataset

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(r"C:\Users\komat\OneDrive\Desktop\intern\data.csv")

# Display Dataset
print("Original Dataset:\n")
print(df)

# Dataset Information
print("\nDataset Info:\n")
print(df.info())

# Check Missing Values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert data into proper format
# Melt the dataset for visualization
df_melted = df.melt(id_vars='Month',
                    var_name='Year',
                    value_name='Passengers')

# Convert Passengers column to numeric
df_melted['Passengers'] = pd.to_numeric(df_melted['Passengers'])

# Display Cleaned Data
print("\nCleaned Dataset:\n")
print(df_melted.head())

# Save Cleaned Dataset
df_melted.to_csv("cleaned_data.csv", index=False)

print("\nData Cleaning Completed Successfully!")

# ---------------- VISUALIZATION ---------------- #

# Line Plot
plt.figure(figsize=(10,5))
sns.lineplot(data=df_melted,
             x='Month',
             y='Passengers',
             hue='Year',
             marker='o')

plt.title("Air Travel Passengers Over Years")
plt.xticks(rotation=45)
plt.show()

# Bar Plot
plt.figure(figsize=(10,5))
sns.barplot(data=df_melted,
            x='Month',
            y='Passengers',
            hue='Year')

plt.title("Monthly Passenger Comparison")
plt.xticks(rotation=45)
plt.show()

# Heatmap
pivot_table = df_melted.pivot(index='Month',
                              columns='Year',
                              values='Passengers')

plt.figure(figsize=(8,6))
sns.heatmap(pivot_table,
            annot=True,
            cmap='YlGnBu')

plt.title("Passenger Heatmap")
plt.show()

print("\nVisualization Completed Successfully!")