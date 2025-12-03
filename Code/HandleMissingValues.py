from sklearn.impute import SimpleImputer

print("Imputing missing values using median strategy...")
imputer = SimpleImputer(strategy='median')
X_imputed = pd.DataFrame(imputer.fit_transform(X_raw), columns=X_raw.columns)

print("Missing values after imputation:")
print(X_imputed.isnull().sum().sum())

