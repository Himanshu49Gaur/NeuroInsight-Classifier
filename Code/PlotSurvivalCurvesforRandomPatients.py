print("Plotting survival curves for 3 random patients...")

sample_indices = np.random.choice(X_predict.index, size=3, replace=False)

plt.figure(figsize=(10, 6))
for i in sample_indices:
    surv_fn = aft.predict_survival_function(X_predict.iloc[[i]])
    plt.step(surv_fn.index, surv_fn.values.flatten(), label=f'Patient {i}')

plt.title("Survival Probability Curves for 3 Patients")
plt.xlabel("Time (e.g., hours)")
plt.ylabel("Survival Probability")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

