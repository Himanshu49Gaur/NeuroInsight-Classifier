from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

print("Preprocessing features...")

X_raw = df.drop(columns=['SepsisLabel', 'duration'])
y = df[[event_col, 'duration']]

# Handle missing values
imputer = SimpleImputer(strategy='median')
X_imputed = pd.DataFrame(imputer.fit_transform(X_raw), columns=X_raw.columns)

# Scale features
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_imputed), columns=X_imputed.columns)

# Combine features + target
X_scaled['duration'] = y['duration']
X_scaled['SepsisLabel'] = y[event_col]

print("Preprocessing complete. Final shape:", X_scaled.shape)

