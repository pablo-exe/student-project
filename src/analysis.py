# File: csv_analyzer.py

# Import required libraries
import pandas as pd
import numpy as np

def load_csv_file(file_path):
    """Load CSV file and return a DataFrame"""
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None
    except Exception as e:
        print(f"Error loading file: {str(e)}")
        return None

def analyze_data(df):
    """Perform basic analysis on the DataFrame"""
    if df is not None:
        # Show basic info about the dataset
        print("\nDataset Info:")
        print(df.info())
        
        # Display first few rows
        print("\nFirst 5 rows:")
        print(df.head())
        
        # Basic statistics
        print("\nBasic Statistics:")
        print(df.describe())
        
        # Check for missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

def clean_data(df):
    """Basic data cleaning operations"""
    if df is not None:
        # Create a copy to avoid modifying original
        cleaned_df = df.copy()
        
        # Fill missing numerical values with mean
        numeric_columns = cleaned_df.select_dtypes(include=[np.number]).columns
        cleaned_df[numeric_columns] = cleaned_df[numeric_columns].fillna(cleaned_df[numeric_columns].mean())
        
        # Fill missing categorical values with mode
        categorical_columns = cleaned_df.select_dtypes(include=['object']).columns
        cleaned_df[categorical_columns] = cleaned_df[categorical_columns].fillna(cleaned_df[categorical_columns].mode().iloc[0])
        
        return cleaned_df

def main():
    # Specify your CSV file path
    file_path = "data.csv"  # Replace with your actual CSV file path
    
    # Load the data
    df = load_csv_file(file_path)
    
    if df is not None:
        # Analyze the original data
        analyze_data(df)
        
        # Clean the data
        cleaned_df = clean_data(df)
        
        # Save cleaned data to new CSV
        cleaned_df.to_csv("cleaned_data.csv", index=False)
        print("\nCleaned data saved to 'cleaned_data.csv'")

if __name__ == "__main__":
    main()