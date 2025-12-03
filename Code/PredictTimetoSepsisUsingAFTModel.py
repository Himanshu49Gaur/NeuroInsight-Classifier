print("Predicting expected time to sepsis...")

# Remove label/duration to form prediction set
X_predict = X_scaled.drop(columns=['duration', 'SepsisLabel'])

# Predict expected survival time (median)
predicted_times = aft.predict_median(X_predict)

# Show results for first 10 patients
prediction_df = df.copy()
prediction_df['Predicted_Sepsis_Time'] = predicted_times.round(2)

print("Sample predictions (in hours/days):")
print(prediction_df[['SepsisLabel', 'Predicted_Sepsis_Time']].head(10))

