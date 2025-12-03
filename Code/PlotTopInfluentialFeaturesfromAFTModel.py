import matplotlib.pyplot as plt

print("Plotting top 5 influential features based on time ratios...")

# Filter to 'lambda_' coefficients only (ignores intercepts and scale parameters)
lambda_coefs = aft.summary.loc[aft.summary.index.get_level_values(0) == 'lambda_']
lambda_coefs = lambda_coefs.sort_values(by='coef', ascending=False)

# Extract clean feature names
top_features = lambda_coefs.head(5)
feature_names = [i[1] for i in top_features.index]

plt.figure(figsize=(8, 5))
plt.barh(feature_names[::-1], top_features['coef'][::-1], color='steelblue')
plt.xlabel("Effect on log(survival time)")
plt.title("Top 5 Influential Features (Weibull AFT)")
plt.grid(True)
plt.tight_layout()
plt.show()

