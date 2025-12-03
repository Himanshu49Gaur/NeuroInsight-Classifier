from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

print("Training base models: Logistic Regression, Random Forest, Gradient Boosting...")
base_models = [
    ('log_reg', LogisticRegression(max_iter=500)),
    ('random_forest', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('gbc', GradientBoostingClassifier(n_estimators=100, random_state=42))
]

base_preds = []
for name, model in base_models:
    print(f"Training {name}...")
    model.fit(X_base, y_base)
    pred = model.predict_proba(X_holdout)[:, 1]
    base_preds.append(pred)

