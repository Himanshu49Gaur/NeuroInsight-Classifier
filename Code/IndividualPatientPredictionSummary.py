example_idx = 7  # Change index to analyze a different patient

# Extract actual and predicted details
actual_event = comparison_df.iloc[example_idx]['SepsisLabel']
predicted_time = comparison_df.iloc[example_idx]['Predicted_Sepsis_Time']
observed_time = comparison_df.iloc[example_idx]['Simulated_Observed_Duration']

# Display result
print(f"Patient {example_idx} Prediction Summary")
print("-" * 40)
print(f"Actual Sepsis Event:        {'Yes' if actual_event == 1 else 'No'}")
print(f"Predicted Time to Sepsis:   {predicted_time} hours/days")
print(f"Observed Monitoring Time:   {observed_time} hours/days")

