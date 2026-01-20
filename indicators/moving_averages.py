"""Moving average indicators."""
import pandas as pd


def sma(data: pd.Series, period: int) -> pd.Series:
    """Calculate Simple Moving Average.
    
    Args:
        data: Price data (typically closing prices)
        period: Number of periods for the moving average
    
    Returns:
        Series containing the simple moving average
    """
    return data.rolling(window=period).mean()


def ema(data: pd.Series, period: int) -> pd.Series:
    """Calculate Exponential Moving Average.
    
    Args:
        data: Price data (typically closing prices)
        period: Number of periods for the moving average
    
    Returns:
        Series containing the exponential moving average
    """
    return data.ewm(span=period, adjust=False).mean()
