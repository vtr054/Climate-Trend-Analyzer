import pandas as pd
import numpy as np

def clean_data(df):
    """
    Cleans the dataset by handling missing values and ensuring correct types.
    """
    df = df.copy()
    
    # Standardize date format
    df['date'] = pd.to_datetime(df['date'])
    
    # Fill missing values if any (using interpolation for time-series)
    if df.isnull().values.any():
        df = df.sort_values('date')
        df = df.interpolate(method='linear')
        
    return df

def feature_engineering(df):
    """
    Creates additional features from the date column and climate readings.
    """
    df = df.copy()
    
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_year'] = df['date'].dt.dayofyear
    
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Autumn'
            
    df['season'] = df['month'].apply(get_season)
    
    # Rolling averages for all numeric columns
    numeric_cols = ['temperature', 'humidity', 'wind_speed', 'meanpressure']
    for col in numeric_cols:
        if col in df.columns:
            df[f'{col}_roll_30'] = df[col].rolling(window=30, center=True).mean()
            df[f'{col}_roll_365'] = df[col].rolling(window=365, center=True).mean()
    
    return df

def preprocess_pipeline(df):
    """Runs the full preprocessing pipeline."""
    df = clean_data(df)
    df = feature_engineering(df)
    return df

if __name__ == "__main__":
    # Test on Delhi data
    from data_loader import load_delhi_data
    try:
        raw_data = load_delhi_data()
        clean_df = preprocess_pipeline(raw_data)
        print(clean_df.head())
        print("\nColumns after engineering:", clean_df.columns.tolist())
    except Exception as e:
        print(f"Error in preprocessing test: {e}")
