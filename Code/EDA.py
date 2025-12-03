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

# ---- 6. Line plot (mean feature trends) ----
print("Generating line plot of mean trends by label...")
plt.figure(figsize=(8, 5))
df.groupby('SepsisLabel')[['HR', 'O2Sat', 'Temp', 'MAP']].mean().T.plot(marker='o')
plt.title("Mean Feature Trends by Sepsis Label")
plt.ylabel("Mean Value")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---- 7. Scatter plot (HR vs Temp) ----
print("Generating scatter plot...")
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='HR', y='Temp', hue='SepsisLabel', alpha=0.6)
plt.title("Scatter Plot: HR vs Temp")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---- 8. Histogram of key features ----
print("Generating histograms...")
features = ['HR', 'O2Sat', 'Temp', 'MAP']
for feature in features:
    plt.figure(figsize=(6, 4))
    sns.histplot(data=df, x=feature, hue='SepsisLabel', kde=True, bins=30, element="step")
    plt.title(f"Histogram of {feature}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
