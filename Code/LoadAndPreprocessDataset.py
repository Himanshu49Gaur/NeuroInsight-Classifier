import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

print("Loading and preprocessing dataset...")
df = pd.read_csv("/kaggle/input/prediction-of-sepsis/Dataset.csv")
df = df.drop(columns=['patient_id', 'timestamp_epoch', 'datetime'], errors='ignore')

X_raw = df.drop(columns=['SepsisLabel'])
y = df['SepsisLabel']

imputer = SimpleImputer(strategy='median')
X_imputed = pd.DataFrame(imputer.fit_transform(X_raw), columns=X_raw.columns)
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_imputed), columns=X_imputed.columns)

