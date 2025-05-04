import pandas as pd

dataset= pd.read_csv('Walmart.csv')

print("Dataset loaded")

columns = ["Weekly_Sales","Holiday_Flag","Temperature","Fuel_Price","CPI",]

for column in columns:
    print(f"Mean: {dataset[column].mean()}")
    print(f"Median: {dataset[column].median()}")
    print(f"Mode: {dataset[column].mode()}")