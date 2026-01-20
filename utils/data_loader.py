"""Data loading utilities."""
import pandas as pd
import numpy as np


def load_csv_data(filepath: str, date_column: str = 'Date', 
                 parse_dates: bool = True) -> pd.DataFrame:
    """Load OHLCV data from CSV file.
    
    Args:
        filepath: Path to the CSV file
        date_column: Name of the date column (default: 'Date')
        parse_dates: Whether to parse dates (default: True)
    
    Returns:
        DataFrame with OHLCV data indexed by date
    """
    df = pd.read_csv(filepath, parse_dates=[date_column] if parse_dates else None)
    
    if parse_dates:
        df.set_index(date_column, inplace=True)
    
    # Ensure required columns exist
    required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Required column '{col}' not found in CSV file")
    
    return df


def generate_sample_data(start_date: str = '2020-01-01', 
                        end_date: str = '2023-12-31',
                        initial_price: float = 100.0,
                        random_seed: int = 42) -> pd.DataFrame:
    """Generate sample OHLCV data for testing.
    
    Args:
        start_date: Start date for the data (default: '2020-01-01')
        end_date: End date for the data (default: '2023-12-31')
        initial_price: Initial price (default: 100.0)
        random_seed: Random seed for reproducibility (default: 42)
    
    Returns:
        DataFrame with sample OHLCV data
    """
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Generate random price movements
    np.random.seed(random_seed)
    returns = np.random.normal(0.001, 0.02, len(dates))
    prices = initial_price * (1 + returns).cumprod()
    
    # Generate OHLCV data
    data = pd.DataFrame({
        'Open': prices * (1 + np.random.uniform(-0.01, 0.01, len(dates))),
        'High': prices * (1 + np.random.uniform(0, 0.02, len(dates))),
        'Low': prices * (1 - np.random.uniform(0, 0.02, len(dates))),
        'Close': prices,
        'Volume': np.random.randint(1000000, 10000000, len(dates))
    }, index=dates)
    
    return data
