from xgboost import XGBClassifier

print("Selecting top 30 features using XGBoost...")
xgb_fs = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
xgb_fs.fit(X_scaled, y)

importances = pd.Series(xgb_fs.feature_importances_, index=X_scaled.columns)
top_features = importances.sort_values(ascending=False).head(30).index.tolist()
X = X_scaled[top_features]

