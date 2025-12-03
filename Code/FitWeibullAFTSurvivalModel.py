from lifelines import WeibullAFTFitter

print("Fitting Weibull AFT survival regression model...")

aft = WeibullAFTFitter()
aft.fit(X_scaled, duration_col='duration', event_col='SepsisLabel')

aft.print_summary()  # Shows coefficients and time ratio effects

