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

# ---- 2. Generating correlation heatmap ----
print("Generating correlation heatmap...")
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), cmap='coolwarm', annot=False, linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

# ---- 3. Pairwise feature distributions ----
print("Generating pairwise feature distributions (pairplot)...")
selected_features = ['HR', 'O2Sat', 'Temp', 'MAP', 'SepsisLabel']
sns.pairplot(df[selected_features], hue='SepsisLabel', plot_kws={'alpha': 0.5})
plt.suptitle("Pairwise Feature Distributions by Sepsis Status", y=1.02)
plt.show()

# ---- 4. Violin plots ----
print("Generating violin plots...")
for feature in ['HR', 'O2Sat', 'Temp', 'MAP']:
    plt.figure(figsize=(6, 4))
    sns.violinplot(x='SepsisLabel', y=feature, data=df)
    plt.title(f"Violin Plot of {feature} by SepsisLabel")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ---- 5. Box plots ----
print("Generating box plots...")
for feature in ['HR', 'O2Sat', 'Temp', 'MAP']:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='SepsisLabel', y=feature, data=df)
    plt.title(f"Box Plot of {feature} by SepsisLabel")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


