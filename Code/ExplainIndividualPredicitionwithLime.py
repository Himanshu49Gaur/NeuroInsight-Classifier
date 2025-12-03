import lime
import lime.lime_tabular

print("Explaining a prediction with LIME...")

# Build explainer
lime_explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=meta_X,
    feature_names=[name for name, _ in base_models],
    class_names=['No Sepsis', 'Sepsis'],
    mode='classification'
)

# Pick a test sample
sample_index = 5  # Choose any valid index
lime_exp = lime_explainer.explain_instance(meta_test_X[sample_index], meta_model.predict_proba)

# Show explanation in notebook
lime_exp.show_in_notebook(show_table=True)

