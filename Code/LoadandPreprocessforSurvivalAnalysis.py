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

# Separate features and label
print("Separating features and target...")
X_raw = df.drop(columns=['SepsisLabel'])
y = df['SepsisLabel']
print(f"Features shape: {X_raw.shape}, Target shape: {y.shape}")

# Handle missing values
print("Imputing missing values with median strategy...")
imputer = SimpleImputer(strategy='median')
X_imputed = pd.DataFrame(imputer.fit_transform(X_raw), columns=X_raw.columns)
print("Missing value imputation complete.")

# Scale features
print("Scaling features using StandardScaler...")
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_imputed), columns=X_imputed.columns)
print("Feature scaling complete.")

print(" Data preprocessing completed successfully!")
