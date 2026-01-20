# Data Directory

This directory is for storing market data files.

## Supported Formats

The framework supports CSV files with the following structure:

```
Date,Open,High,Low,Close,Volume
2020-01-01,100.00,102.50,99.50,101.00,1000000
2020-01-02,101.00,103.00,100.50,102.50,1200000
...
```

## Required Columns

- **Date**: Trading date (format: YYYY-MM-DD)
- **Open**: Opening price
- **High**: Highest price of the day
- **Low**: Lowest price of the day
- **Close**: Closing price
- **Volume**: Trading volume

## Loading Data

Use the data loader utility to load your CSV files:

```python
from utils.data_loader import load_csv_data

# Load data from CSV
data = load_csv_data('data/your_data.csv')
```

## Data Sources

You can obtain historical market data from various sources:

- **Yahoo Finance**: https://finance.yahoo.com/
- **Alpha Vantage**: https://www.alphavantage.co/
- **Quandl**: https://www.quandl.com/
- **IEX Cloud**: https://iexcloud.io/

## Sample Data

For testing purposes, you can generate sample data:

```python
from utils.data_loader import generate_sample_data

# Generate sample data
data = generate_sample_data(
    start_date='2020-01-01',
    end_date='2023-12-31',
    initial_price=100.0
)
```

## Note

Add your data files here but remember to add `*.csv` to `.gitignore` if you don't want to commit large data files to the repository.
