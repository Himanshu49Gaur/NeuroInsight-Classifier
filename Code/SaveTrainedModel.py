import joblib
import os

# Create output directory if it doesn't exist
os.makedirs("/kaggle/working/models", exist_ok=True)

# Save base models
for name, model in base_models:
    joblib.dump(model, f"/kaggle/working/models/base_model_{name}.pkl")
    print(f"Saved base model: {name}")

# Save meta model
joblib.dump(meta_model, "/kaggle/working/models/meta_model_xgb.pkl")
print("Meta-model saved successfully to /kaggle/working/models")

