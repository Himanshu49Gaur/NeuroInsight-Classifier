import pandas as pd

print("Loading dataset...")
data_path = "/kaggle/input/prediction-of-sepsis/Dataset.csv"
df = pd.read_csv(data_path)
print("First 5 rows of the dataset:")
print(df.head())

