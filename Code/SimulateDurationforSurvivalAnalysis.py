import pandas as pd
import numpy as np

print("Loading dataset...")
df = pd.read_csv("/kaggle/input/prediction-of-sepsis/Dataset.csv")
print("Initial shape:", df.shape)

# Drop non-feature columns (if any)
df = df.drop(columns=['patient_id', 'datetime', 'timestamp_epoch'], errors='ignore')

# Define label
event_col = 'SepsisLabel'

# Simulate duration (e.g., time until diagnosis or monitoring window)
np.random.seed(42)
df['duration'] = np.random.randint(30, 100, size=len(df))  # Simulated hours/days

# Final dataset
print("Prepared dataset:")
print(df[[event_col, 'duration']].head())

