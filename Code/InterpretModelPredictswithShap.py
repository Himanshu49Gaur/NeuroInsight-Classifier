import shap

print("Explaining model predictions with SHAP...")

# Use meta_X from earlier (the stacked feature set)
explainer = shap.Explainer(meta_model, meta_X)
shap_values = explainer(meta_X)

# Global explanation
shap.summary_plot(shap_values, features=meta_X, feature_names=[name for name, _ in base_models])

