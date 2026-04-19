from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def calculate_trends(df, target_col='temperature'):
    """
    Calculates the linear trend of a target column.
    """
    # Prepare X (days as integers) and y
    X = np.arange(len(df)).reshape(-1, 1)
    y = df[target_col].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    slope = model.coef_[0]
    intercept = model.intercept_
    
    # Yearly trend (365.25 days)
    yearly_slope = slope * 365.25
    
    return {
        'column': target_col,
        'slope_per_day': slope,
        'yearly_trend': yearly_slope,
        'intercept': intercept
    }

def get_monthly_averages(df):
    """Calculates monthly averages across all years for available metrics."""
    cols = [c for c in ['temperature', 'humidity', 'wind_speed', 'meanpressure'] if c in df.columns]
    return df.groupby('month')[cols].mean()

def get_yearly_stats(df):
    """Calculates summary statistics per year."""
    agg_map = {
        'temperature': ['mean', 'max', 'min'],
        'humidity': 'mean'
    }
    if 'wind_speed' in df.columns:
        agg_map['wind_speed'] = ['mean', 'max']
    if 'meanpressure' in df.columns:
        agg_map['meanpressure'] = 'mean'
        
    return df.groupby('year').agg(agg_map)

if __name__ == "__main__":
    # Test on Delhi data
    from data_loader import load_delhi_data
    from preprocessing import preprocess_pipeline
    
    try:
        df = preprocess_pipeline(load_delhi_data())
        trend = calculate_trends(df)
        print(f"Delhi Temperature Trend: {trend['yearly_trend']:.4f}C per year")
        
        stats = get_yearly_stats(df)
        print("\nDelhi Yearly Stats:")
        print(stats)
    except Exception as e:
        print(f"Error in analysis test: {e}")
