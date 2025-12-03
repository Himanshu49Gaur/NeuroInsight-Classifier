import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

print("Loading dataset...")
df = pd.read_csv("/kaggle/input/prediction-of-sepsis/Dataset.csv")
print(f"Dataset loaded successfully. Shape: {df.shape}")

# Drop unused columns
print("Dropping unused columns (if present)...")
df = df.drop(columns=['patient_id', 'timestamp_epoch', 'datetime'], errors='ignore')
print(f"Remaining columns: {df.columns.tolist()}")

