print("Cleaning column names...")
def clean_column_names(df):
    return [col.replace('"', '').replace('\\', '').replace(' ', '_')
                .replace('[', '').replace(']', '')
                .replace('{', '').replace('}', '')
                .replace(':', '').replace(',', '') for col in df.columns]

X.columns = clean_column_names(X)
