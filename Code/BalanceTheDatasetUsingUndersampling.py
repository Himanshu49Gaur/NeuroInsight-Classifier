df_bal = pd.concat([X, y], axis=1)
class_0 = df_bal[df_bal['SepsisLabel'] == 0]
class_1 = df_bal[df_bal['SepsisLabel'] == 1]
class_0_down = class_0.sample(n=len(class_1), random_state=42)
df_balanced = pd.concat([class_1, class_0_down]).sample(frac=1, random_state=42)
X_bal = df_balanced.drop(columns=['SepsisLabel'])
y_bal = df_balanced['SepsisLabel']

print("Balanced dataset class distribution:")
print(y_bal.value_counts())
