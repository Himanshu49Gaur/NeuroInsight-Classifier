from sklearn.utils.class_weight import compute_sample_weight
from sklearn.model_selection import train_test_split

print("Computing sample weights using class balance...")
sample_weights = compute_sample_weight(class_weight="balanced", y=y)

print("Performing initial train-test split (85% temp, 15% test)...")
X_temp, X_test, y_temp, y_test, sw_temp, sw_test = train_test_split(
    X_scaled, y, sample_weights, test_size=0.15, stratify=y, random_state=42
)

print("Performing train-validation split from temp set (85% train, 15% validation)...")
X_train, X_val, y_train, y_val, w_train, w_val = train_test_split(
    X_temp, y_temp, sw_temp, test_size=0.15, stratify=y_temp, random_state=42
)

print(f"Shapes:")
print(f"  Train:      {X_train.shape}, Labels: {y_train.shape}, Weights: {w_train.shape}")
print(f"  Validation: {X_val.shape}, Labels: {y_val.shape}, Weights: {w_val.shape}")
print(f"  Test:       {X_test.shape}, Labels: {y_test.shape}, Weights: {sw_test.shape}")

