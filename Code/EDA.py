import matplotlib.pyplot as plt
import seaborn as sns

print("Performing Enhanced Exploratory Data Analysis (EDA)...")

# ---- 1. Visualizing distribution of SepsisLabel ----
print("Visualizing distribution of SepsisLabel...")
plt.figure(figsize=(6, 4))
sns.countplot(x='SepsisLabel', data=df)
plt.title("Sepsis Label Distribution")
plt.xlabel("Sepsis Label")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()


