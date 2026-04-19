import pandas as pd
import numpy as np
import os

def generate_synthetic_data(start_date='2014-01-01', periods=3652):
    """
    Generates a synthetic climate dataset with realistic patterns.
    
    Args:
        start_date (str): Starting date for the dataset.
        periods (int): Number of days to generate (default 10 years).
        
    Returns:
        pd.DataFrame: Synthetic climate data.
    """
    np.random.seed(42)
    dates = pd.date_range(start=start_date, periods=periods, freq='D')
    
    # 1. Temperature: Seasonal Sine Wave + Linear Growth + Noise
    # Base temp ≈ 15°C, Amplitude ≈ 10°C
    day_of_year = dates.dayofyear
    seasonal_temp = 10 * np.sin(2 * np.pi * day_of_year / 365.25)
    
    # Linear warming trend of 0.1°C per year (1°C per decade)
    days_passed = np.arange(len(dates))
    warming_trend = 0.1 * (days_passed / 365.25)
    
    temp_noise = np.random.normal(0, 1.5, size=len(dates))
    temperature = 15 + seasonal_temp + warming_trend + temp_noise
    
    # 2. Rainfall: Seasonal Gamma distribution
    # More rain in 'winter' months (assuming North hemisphere for simplicity)
    seasonal_rain_prob = 0.5 * (np.sin(2 * np.pi * day_of_year / 365.25 + np.pi/2) + 1)
    rain_occurence = np.random.binomial(1, 0.2 + 0.3 * seasonal_rain_prob)
    rain_amount = np.random.gamma(2, 5, size=len(dates)) * rain_occurence
    
    # Add some extreme events (anomalies)
    extreme_rain_indices = np.random.choice(len(dates), size=10, replace=False)
    for idx in extreme_rain_indices:
        rain_amount[idx] += 50  # Heavy burst
        
    # 3. Humidity: Inversely correlated with temperature + Noise
    humidity_base = 100 - (temperature * 1.5)
    humidity_noise = np.random.normal(0, 5, size=len(dates))
    humidity = np.clip(humidity_base + humidity_noise, 30, 95)
    
    df = pd.DataFrame({
        'date': dates,
        'temperature': temperature,
        'rainfall': rain_amount,
        'humidity': humidity
    })
    
    return df

def load_delhi_data(train_path='data/DailyDelhiClimateTrain.csv', test_path='data/DailyDelhiClimateTest.csv'):
    """
    Loads and merges the Daily Delhi Climate Train and Test datasets.
    Renames columns for consistency.
    """
    if not os.path.exists(train_path):
        raise FileNotFoundError(f"Missing training data at {train_path}")
        
    train_df = pd.read_csv(train_path)
    
    # Load test data if available
    if os.path.exists(test_path):
        test_df = pd.read_csv(test_path)
        df = pd.concat([train_df, test_df], ignore_index=True)
        print(f"Merged {len(train_df)} train and {len(test_df)} test records.")
    else:
        df = train_df
        print(f"Loaded {len(train_df)} train records only (Test file missing).")
        
    # Standardize column names
    rename_map = {
        'meantemp': 'temperature',
        'humidity': 'humidity',
        'wind_speed': 'wind_speed',
        'meanpressure': 'meanpressure'
    }
    df = df.rename(columns=rename_map)
    df['date'] = pd.to_datetime(df['date'])
    
    return df

def save_data(df, filepath='data/climate_raw.csv'):
    """Saves the dataframe to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

if __name__ == "__main__":
    # Test load
    try:
        data = load_delhi_data()
        print("\nDelhi Data loaded successfully:")
        print(data.head())
        print(data.info())
    except Exception as e:
        print(f"Error loading Delhi data: {e}")
        print("Falling back to synthetic data...")
        data = generate_synthetic_data()
        print(data.head())
