"""Momentum indicators."""
import pandas as pd


def rsi(data: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Relative Strength Index.
    
    Args:
        data: Price data (typically closing prices)
        period: Number of periods for RSI calculation (default: 14)
    
    Returns:
        Series containing the RSI values (0-100)
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi


def macd(data: pd.Series, fast_period: int = 12, slow_period: int = 26, 
         signal_period: int = 9) -> pd.DataFrame:
    """Calculate MACD (Moving Average Convergence Divergence).
    
    Args:
        data: Price data (typically closing prices)
        fast_period: Fast EMA period (default: 12)
        slow_period: Slow EMA period (default: 26)
        signal_period: Signal line period (default: 9)
    
    Returns:
        DataFrame with columns: 'macd', 'signal', 'histogram'
    """
    fast_ema = data.ewm(span=fast_period, adjust=False).mean()
    slow_ema = data.ewm(span=slow_period, adjust=False).mean()
    
    macd_line = fast_ema - slow_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    histogram = macd_line - signal_line
    
    return pd.DataFrame({
        'macd': macd_line,
        'signal': signal_line,
        'histogram': histogram
    })
