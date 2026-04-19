import numpy as np
import pandas as pd
from scipy import stats

def detect_anomalies_zscore(df, column='temperature', threshold=3):
    """
    Detects anomalies using Z-score.
    
    Args:
        df (pd.DataFrame): The dataset.
        column (str): Column to analyze.
        threshold (float): Z-score threshold (default 3).
        
    Returns:
        pd.DataFrame: A dataframe containing only the anomalous records.
    """
    df_clean = df.copy()
    z_scores = np.abs(stats.zscore(df_clean[column]))
    df_clean[f'{column}_zscore'] = z_scores
    
    anomalies = df_clean[df_clean[f'{column}_zscore'] > threshold]
    return anomalies

def get_extreme_weather_events(df):
    """
    Combines temperature and wind speed anomalies to identify extreme weather.
    """
    temp_anomalies = detect_anomalies_zscore(df, 'temperature', threshold=2.5)
    
    combined_list = [temp_anomalies]
    temp_anomalies['event_type'] = 'Temperature Anomaly'
    
    if 'wind_speed' in df.columns:
        wind_anomalies = detect_anomalies_zscore(df, 'wind_speed', threshold=3.5)
        wind_anomalies['event_type'] = 'Extreme Wind Event'
        combined_list.append(wind_anomalies)
    
    combined = pd.concat(combined_list).sort_values('date')
    return combined

if __name__ == "__main__":
    # Test on Delhi data
    from data_loader import load_delhi_data
    from preprocessing import preprocess_pipeline
    
    try:
        df = preprocess_pipeline(load_delhi_data())
        anomalies = get_extreme_weather_events(df)
        print(f"Total Delhi anomalies detected: {len(anomalies)}")
        print(anomalies[['date', 'temperature', 'event_type']].head())
    except Exception as e:
        print(f"Error in anomaly test: {e}")
