print("Creating custom test set:")
test_df = pd.concat([X, y], axis=1)
class_0 = test_df[test_df['SepsisLabel'] == 0].sample(n=5584, random_state=42)
class_1 = test_df[test_df['SepsisLabel'] == 1].sample(n=5583, random_state=42)
test_balanced_df = pd.concat([class_0, class_1]).sample(frac=1, random_state=42)
X_test_balanced = test_balanced_df.drop(columns=['SepsisLabel'])
y_test_balanced = test_balanced_df['SepsisLabel']
