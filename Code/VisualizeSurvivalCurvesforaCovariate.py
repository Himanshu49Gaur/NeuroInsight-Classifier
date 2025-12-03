import matplotlib.pyplot as plt

print("Plotting survival function based on a single covariate...")


covariate_name = X_predict.columns[0]  
values_to_test = [-1, 0, 1]  
aft.plot_partial_effects_on_outcome(
    covariates=covariate_name,
    values=values_to_test,
    cmap='coolwarm'
)

plt.title(f"Weibull AFT – Survival Curve vs. {covariate_name}")
plt.xlabel("Time (e.g., hours)")
plt.ylabel("Survival Probability")
plt.grid(True)
plt.tight_layout()
plt.show()

