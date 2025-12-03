from sklearn.metrics import classification_report, precision_recall_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

print("Evaluating final model on custom balanced test set...")
base_test_preds = [model.predict_proba(X_test_balanced)[:, 1] for _, model in base_models]
meta_test_X = np.column_stack(base_test_preds)
y_scores = meta_model.predict_proba(meta_test_X)[:, 1]

precision, recall, thresholds = precision_recall_curve(y_test_balanced, y_scores)
f1_scores = 2 * (precision * recall) / (precision + recall + 1e-8)
best_thresh = thresholds[np.argmax(f1_scores)]

print(f"\nOptimal Threshold for F1: {best_thresh:.3f}")
final_preds = (y_scores >= best_thresh).astype(int)

print("\nClassification Report:")
print(classification_report(y_test_balanced, final_preds))
print("ROC AUC Score:", roc_auc_score(y_test_balanced, y_scores))

plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y_test_balanced, final_preds), annot=True, fmt='d', cmap='YlGnBu')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
