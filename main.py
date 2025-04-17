# main.py
from data_collection.collect_data import load_data
from data_processing.eda_analysis import run_eda
from data_processing.process import preprocess_data
from database.create_db import save_to_db

def main():

    
    # Step 1: Load the data
    df = load_data()  
    print("Data Loaded Successfully!")
    
    # Step 2: Run Exploratory Data Analysis (EDA)
    run_eda(df)  
    print("EDA Completed!")

    # Step 3: Preprocess the data
    df_clean = preprocess_data(df)  
    print("Data Preprocessing Completed!")
    
    # list column names
    print("📋 DataFrame columns before saving:")
    print(df.columns.tolist())

    # Preview of preprocessed data
    print("\n--- Preprocessed Data Preview ---")
    print(df_clean.head())

    # Step 4: Save the cleaned data to the database
    # Assuming your DataFrame is already defined (df)
    save_to_db(df)
    print("Data inserted into the database successfully!")


    
if __name__ == "__main__":
    main()

