import pandas as pd

def run_eda(df):
    """
    Runs basic EDA (Exploratory Data Analysis) on the given DataFrame.
    Prints dataset shape, column types, missing values, summary stats, and unique value counts.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
    """
    print("\n--- Shape of the Dataset ---")
    print(df.shape)

    print("\n--- Column Information ---")
    print(df.dtypes)

    print("\n--- Missing Values Per Column ---")
    print(df.isnull().sum())

    print("\n--- Summary Statistics for Numeric Columns ---")
    print(df.describe())

    print("\n--- Unique Values Per Column ---")
    for col in df.columns:
        unique_vals = df[col].nunique()
        print(f"{col}: {unique_vals} unique values")

