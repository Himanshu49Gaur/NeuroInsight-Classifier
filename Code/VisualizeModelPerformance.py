from sklearn.metrics import roc_curve, precision_recall_curve, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

# Compute predictions & scores
base_test_preds = [model.predict_proba(X_test_balanced)[:, 1] for _, model in base_models]
meta_test_X = np.column_stack(base_test_preds)
y_scores = meta_model.predict_proba(meta_test_X)[:, 1]
final_preds = (y_scores >= best_thresh).astype(int)

# Plot 1: Confusion Matrix
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y_test_balanced, final_preds), annot=True, fmt='d', cmap='YlGnBu')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()
