print("Displaying sample predictions (actual vs predicted time)...")

comparison_df = df[['SepsisLabel']].copy()
comparison_df['Predicted_Sepsis_Time'] = predicted_times.round(2)
comparison_df['Simulated_Observed_Duration'] = df['duration']

# Show top 10 rows
print(comparison_df.head(10))

