print("Plotting histogram of predicted time to sepsis...")

plt.figure(figsize=(8, 5))
plt.hist(predicted_times, bins=25, color='salmon', edgecolor='black')
plt.title("Distribution of Predicted Sepsis Onset Times")
plt.xlabel("Predicted Time (hours/days)")
plt.ylabel("Number of Patients")
plt.grid(True)
plt.tight_layout()
plt.show()

