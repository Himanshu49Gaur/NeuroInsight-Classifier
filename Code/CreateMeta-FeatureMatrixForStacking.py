import numpy as np

print("Stacking base model predictions...")
meta_X = np.column_stack(base_preds)
meta_y = y_holdout
