import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def plot_temperature_trend(df, trend_info, save_path='outputs/temp_trend.png'):
    """
    Plots temperature with rolling averages and linear trend line.
    """
    plt.figure()
    
    # Original data (light color)
    sns.lineplot(data=df, x='date', y='temperature', alpha=0.3, label='Daily Temp', color='skyblue')
    
    # Rolling average
    sns.lineplot(data=df, x='date', y='temperature_roll_365', label='365-day Rolling Avg', color='navy', linewidth=2)
    
    # Trend line
    X_days = np.arange(len(df))
    trend_line = trend_info['intercept'] + trend_info['slope_per_day'] * X_days
    plt.plot(df['date'], trend_line, color='red', linestyle='--', label=f"Trend ({trend_info['yearly_trend']:.3f}C/yr)")
    
    plt.title('Delhi Temperature Trend Analysis (2013-2017)', fontsize=15)
    plt.xlabel('Date')
    plt.ylabel('Temperature (C)')
    plt.legend()
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {save_path}")

def plot_seasonal_patterns(df, save_path='outputs/seasonal_patterns.png'):
    """
    Plots average temperature and humidity per month for Delhi.
    """
    fig, ax1 = plt.subplots()

    # Monthly Temperature
    monthly_data = df.groupby('month')[['temperature', 'humidity']].mean().reset_index()
    
    sns.barplot(data=monthly_data, x='month', y='temperature', ax=ax1, palette='coolwarm', alpha=0.7)
    ax1.set_ylabel('Avg Temperature (C)', color='darkred')
    ax1.set_xlabel('Month')
    
    # Humidity on second axis
    ax2 = ax1.twinx()
    sns.lineplot(data=monthly_data, x=monthly_data.index, y='humidity', ax=ax2, color='green', marker='o', linewidth=2)
    ax2.set_ylabel('Avg Humidity (%)', color='green')
    
    plt.title('Seasonal Delhi Temperature and Humidity Patterns', fontsize=15)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {save_path}")

def plot_anomalies(df, anomalies, save_path='outputs/anomalies.png'):
    """
    Highlights anomalies on a temperature timeline.
    """
    plt.figure()
    
    # Plot temperature
    sns.lineplot(data=df, x='date', y='temperature', color='gray', alpha=0.5, label='Actual Temp')
    
    # Mark anomalies
    if not anomalies.empty:
        temp_anom = anomalies[anomalies['event_type'] == 'Temperature Anomaly']
        plt.scatter(temp_anom['date'], temp_anom['temperature'], color='red', s=40, label='Temp Anomaly', zorder=5)
    
    plt.title('Delhi Climate Anomaly Detection', fontsize=15)
    plt.xlabel('Date')
    plt.ylabel('Temperature (C)')
    plt.legend()
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {save_path}")

if __name__ == "__main__":
    # Test on Delhi data
    from data_loader import load_delhi_data
    from preprocessing import preprocess_pipeline
    from analysis import calculate_trends
    from anomaly import get_extreme_weather_events
    
    try:
        df = preprocess_pipeline(load_delhi_data())
        trend = calculate_trends(df)
        anom = get_extreme_weather_events(df)
        
        plot_temperature_trend(df, trend)
        plot_seasonal_patterns(df)
        plot_anomalies(df, anom)
    except Exception as e:
        print(f"Error in visualization test: {e}")
