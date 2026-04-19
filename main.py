import os
import pandas as pd
from src.data_loader import load_delhi_data, save_data
from src.preprocessing import preprocess_pipeline
from src.analysis import calculate_trends, get_yearly_stats
from src.anomaly import get_extreme_weather_events
from src.visualization import plot_temperature_trend, plot_seasonal_patterns, plot_anomalies

def run_project():
    print("="*50)
    print("Project Transition: Daily Delhi Climate Dataset")
    print("="*50)
    
    # 1. Data Ingestion
    print("\n[1/5] Loading and merging Delhi Climate CSVs...")
    raw_df = load_delhi_data()
    save_data(raw_df, 'data/climate_raw.csv')
    
    # 2. Preprocessing
    print("\n[2/5] Cleaning and engineering features for Delhi dataset...")
    processed_df = preprocess_pipeline(raw_df)
    processed_df.to_csv('outputs/processed_delhi_data.csv', index=False)
    
    # 3. Trend Analysis
    print("\n[3/5] Performing trend analysis (Meantemp)...")
    temp_trend = calculate_trends(processed_df, 'temperature')
    yearly_stats = get_yearly_stats(processed_df)
    yearly_stats.to_csv('outputs/delhi_yearly_summary.csv')
    
    print(f"Delhi Trend: {temp_trend['yearly_trend']:.3f}C change per year.")
    
    # 4. Anomaly Detection
    print("\n[4/5] Detecting anomalies in temperature and wind speed...")
    anomalies = get_extreme_weather_events(processed_df)
    anomalies.to_csv('outputs/delhi_detected_anomalies.csv', index=False)
    print(f"Found {len(anomalies)} anomalous weather events in Delhi records.")
    
    # 5. Visualization
    print("\n[5/5] Generating Delhi-specific visualizations...")
    plot_temperature_trend(processed_df, temp_trend, 'outputs/delhi_temperature_trends.png')
    plot_seasonal_patterns(processed_df, 'outputs/delhi_seasonal_patterns.png')
    plot_anomalies(processed_df, anomalies, 'outputs/delhi_anomaly_map.png')
    
    print("\n" + "="*50)
    print("Project Execution Complete!")
    print("Real-world analysis saved to 'outputs/' directory.")
    print("="*50)

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs('outputs', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    run_project()
