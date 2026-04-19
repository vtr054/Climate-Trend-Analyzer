# 🌍 Delhi Climate Trend Analyzer

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Data](https://img.shields.io/badge/Dataset-Kaggle%20Delhi%20Climate-orange.svg)](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-data-in-delhi)

An industry-grade climate analysis pipeline that processes actual historical weather records from Delhi (2013-2017), identifying warming trends and detecting extreme atmospheric anomalies.

## 📌 Project Overview
The **Delhi Climate Trend Analyzer** leverages real-world meteorological data to uncover shifts in regional weather patterns. By merging multiple historical CSV records, this tool provides a multi-year analysis of temperature, humidity, wind speed, and atmospheric pressure.

### Key Features:
- **🌡️ Meantemp Analysis**: Tracks temperature changes with a 333% increase visibility using 365-day rolling averages.
- **💨 Multi-Metric Support**: Expands analysis to include Wind Speed and Mean Pressure.
- **🚨 Real-World Anomalies**: Identifies high-temp spikes and extreme wind events using statistical Z-scores.
- **📊 Professional Visuals**: High-resolution PNG reports tailored for climate research presentation.

---

## 🏗️ Architecture & Workflow
The project follows a modular architecture for scalability and clean code standards.

```text
[ Data Loader ] -> [ Preprocessing ] -> [ Analysis ] -> [ Anomaly Detection ] -> [ Visualization ]
       |                  |                |                  |                   |
  Synthetic Gen.      Cleaning        Linear Trends        Z-Score            Seaborn Plots
```

1.  **Data Generation**: Simulates 10 years of daily readings with seasonal cycles and warming trends.
2.  **Cleaning**: Implements interpolation for missing data and date-time standardization.
3.  **Feature Engineering**: Extracts temporal features (season, month, year) and rolling window stats.
4.  **Modeling**: Conducts least-squares regression to find the rate of change.
5.  **Reporting**: Exporting insights into `outputs/` folder.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- `pip` (Python package manager)

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/climate-trend-analyzer.git
   cd climate-trend-analyzer
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis
To run the complete pipeline:
```bash
python main.py
```

---

## 📂 Project Structure
```text
climate-trend-analyzer/
├── data/               # Raw datasets
├── src/                # Modular source code
│   ├── data_loader.py  # Data ingestion/generation
│   ├── preprocessing.py# Cleaning & feature engineering
│   ├── analysis.py     # Trends & statistics
│   ├── anomaly.py      # Outlier detection
│   └── visualization.py# Plotting tools
├── outputs/            # Processed files & plots (CSV, PNG)
├── main.py             # Orchestration script
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## 📊 Sample Results
The analyzer generates several key outputs:
- `temperature_trends.png`: Visualizes global warming trends over a decade.
- `anomaly_map.png`: Highlights extreme weather dates.
- `yearly_summary_stats.csv`: Annual averages for climate monitoring.

### Future Improvements
- [ ] Integration with real NOAA/NASA APIs for live data.
- [ ] Advanced forecasting using LSTM networks.
- [ ] Interactive dashboard using Streamlit.

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
