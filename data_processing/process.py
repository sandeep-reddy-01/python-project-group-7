import pandas as pd 
def preprocess_data(df):
    """
    Preprocesses the election dataset.
    
    Operations:
    - Drops constant columns
    - Encodes categorical variables using one-hot encoding
    - Normalizes the target/count column
    - Returns cleaned DataFrame
    
    Args:
        df (pd.DataFrame): Raw input DataFrame
    
    Returns:
        pd.DataFrame: Preprocessed DataFrame
    """

    # Drop constant columns
    if 'CounterGroup' in df.columns and df['CounterGroup'].nunique() == 1:
        df = df.drop(columns=['CounterGroup'])

    # Convert categorical columns to category type (for efficient memory use and later encoding)
    categorical_cols = ['Precinct', 'Race', 'CounterType']
    for col in categorical_cols:
        df[col] = df[col].astype('category')

    # Optional: Encode categorical columns using one-hot encoding
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Normalize 'SumOfCount' if needed (min-max scaling as an example)
    if 'SumOfCount' in df.columns:
        df['SumOfCount'] = (df['SumOfCount'] - df['SumOfCount'].min()) / (df['SumOfCount'].max() - df['SumOfCount'].min())

    return df