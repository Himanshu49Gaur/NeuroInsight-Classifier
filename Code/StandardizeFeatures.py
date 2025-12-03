from sklearn.preprocessing import StandardScaler

print("Standardizing features...")
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_imputed), columns=X_imputed.columns)

print("Feature matrix after standardization (first 5 rows):")
print(X_scaled.head())

