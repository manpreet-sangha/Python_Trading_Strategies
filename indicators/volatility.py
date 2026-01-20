"""Volatility indicators."""
import pandas as pd


def bollinger_bands(data: pd.Series, period: int = 20, 
                   num_std: float = 2.0) -> pd.DataFrame:
    """Calculate Bollinger Bands.
    
    Args:
        data: Price data (typically closing prices)
        period: Number of periods for moving average (default: 20)
        num_std: Number of standard deviations for bands (default: 2.0)
    
    Returns:
        DataFrame with columns: 'middle', 'upper', 'lower'
    """
    middle = data.rolling(window=period).mean()
    std = data.rolling(window=period).std()
    
    upper = middle + (std * num_std)
    lower = middle - (std * num_std)
    
    return pd.DataFrame({
        'middle': middle,
        'upper': upper,
        'lower': lower
    })
