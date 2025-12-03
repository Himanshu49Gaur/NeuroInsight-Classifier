example_idx = 3  # Pick any row to demonstrate
actual = prediction_df.iloc[example_idx]['SepsisLabel']
pred_time = prediction_df.iloc[example_idx]['Predicted_Sepsis_Time']

print(f"Patient {example_idx}:")
print(f"  Sepsis event occurred? {'Yes' if actual == 1 else 'No'}")
print(f"  Predicted time to sepsis (or observation end): {pred_time} hours/days")

