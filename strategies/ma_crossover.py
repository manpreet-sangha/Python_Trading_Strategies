"""Moving Average Crossover Strategy."""
import pandas as pd
from .base_strategy import BaseStrategy
from indicators.moving_averages import sma


class MovingAverageCrossover(BaseStrategy):
    """Moving Average Crossover Strategy.
    
    Generates buy signals when short-term MA crosses above long-term MA.
    Generates sell signals when short-term MA crosses below long-term MA.
    """
    
    def __init__(self, short_period: int = 50, long_period: int = 200):
        """Initialize the strategy.
        
        Args:
            short_period: Period for short-term moving average (default: 50)
            long_period: Period for long-term moving average (default: 200)
        """
        super().__init__("Moving Average Crossover")
        self.short_period = short_period
        self.long_period = long_period
        
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate trading signals based on MA crossover.
        
        Args:
            data: DataFrame with OHLCV data
        
        Returns:
            DataFrame with added signal columns
        """
        result = data.copy()
        
        # Calculate moving averages
        result['short_ma'] = sma(result['Close'], self.short_period)
        result['long_ma'] = sma(result['Close'], self.long_period)
        
        # Initialize signal column
        result['signal'] = 0
        
        # Generate signals
        # Buy when short MA crosses above long MA
        result.loc[(result['short_ma'] > result['long_ma']) & 
                   (result['short_ma'].shift(1) <= result['long_ma'].shift(1)), 
                   'signal'] = 1
        
        # Sell when short MA crosses below long MA
        result.loc[(result['short_ma'] < result['long_ma']) & 
                   (result['short_ma'].shift(1) >= result['long_ma'].shift(1)), 
                   'signal'] = -1
        
        self.signals = result
        return result
