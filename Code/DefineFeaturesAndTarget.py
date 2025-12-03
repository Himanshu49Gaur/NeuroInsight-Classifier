print("Dropping unnecessary columns and defining features and target...")
df = df.drop(columns=['patient_id'], errors='ignore')
target_col = 'SepsisLabel'
X_raw = df.drop(columns=[target_col])
y = df[target_col]

print(f"Shape of feature matrix: {X_raw.shape}")
print(f"Target distribution:\n{y.value_counts()}")

