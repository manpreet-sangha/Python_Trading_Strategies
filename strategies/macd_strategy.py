"""MACD Trading Strategy."""
import pandas as pd
from .base_strategy import BaseStrategy
from indicators.momentum import macd


class MACDStrategy(BaseStrategy):
    """MACD (Moving Average Convergence Divergence) Trading Strategy.
    
    Generates buy signals when MACD line crosses above signal line.
    Generates sell signals when MACD line crosses below signal line.
    """
    
    def __init__(self, fast_period: int = 12, slow_period: int = 26, 
                 signal_period: int = 9):
        """Initialize the strategy.
        
        Args:
            fast_period: Fast EMA period (default: 12)
            slow_period: Slow EMA period (default: 26)
            signal_period: Signal line period (default: 9)
        """
        super().__init__("MACD Strategy")
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period
        
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate trading signals based on MACD crossover.
        
        Args:
            data: DataFrame with OHLCV data
        
        Returns:
            DataFrame with added signal columns
        """
        result = data.copy()
        
        # Calculate MACD
        macd_data = macd(result['Close'], self.fast_period, 
                        self.slow_period, self.signal_period)
        result['macd'] = macd_data['macd']
        result['macd_signal'] = macd_data['signal']
        result['macd_histogram'] = macd_data['histogram']
        
        # Initialize signal column
        result['signal'] = 0
        
        # Generate signals
        # Buy when MACD crosses above signal line
        result.loc[(result['macd'] > result['macd_signal']) & 
                   (result['macd'].shift(1) <= result['macd_signal'].shift(1)), 
                   'signal'] = 1
        
        # Sell when MACD crosses below signal line
        result.loc[(result['macd'] < result['macd_signal']) & 
                   (result['macd'].shift(1) >= result['macd_signal'].shift(1)), 
                   'signal'] = -1
        
        self.signals = result
        return result
