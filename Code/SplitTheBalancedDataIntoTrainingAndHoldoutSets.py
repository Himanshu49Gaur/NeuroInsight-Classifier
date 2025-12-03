from sklearn.model_selection import train_test_split

X_base, X_holdout, y_base, y_holdout = train_test_split(
    X_bal, y_bal, test_size=0.2, stratify=y_bal, random_state=42
)
