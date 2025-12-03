import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

print("Loading dataset...")
df = pd.read_csv("/kaggle/input/prediction-of-sepsis/Dataset.csv")
print(f"Dataset loaded successfully. Shape: {df.shape}")
