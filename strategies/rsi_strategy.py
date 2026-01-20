"""RSI Trading Strategy."""
import pandas as pd
from .base_strategy import BaseStrategy
from indicators.momentum import rsi


class RSIStrategy(BaseStrategy):
    """RSI (Relative Strength Index) Trading Strategy.
    
    Generates buy signals when RSI crosses below oversold threshold.
    Generates sell signals when RSI crosses above overbought threshold.
    """
    
    def __init__(self, period: int = 14, oversold: int = 30, overbought: int = 70):
        """Initialize the strategy.
        
        Args:
            period: RSI calculation period (default: 14)
            oversold: Oversold threshold (default: 30)
            overbought: Overbought threshold (default: 70)
        """
        super().__init__("RSI Strategy")
        self.period = period
        self.oversold = oversold
        self.overbought = overbought
        
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate trading signals based on RSI levels.
        
        Args:
            data: DataFrame with OHLCV data
        
        Returns:
            DataFrame with added signal columns
        """
        result = data.copy()
        
        # Calculate RSI
        result['rsi'] = rsi(result['Close'], self.period)
        
        # Initialize signal column
        result['signal'] = 0
        
        # Generate signals
        # Buy when RSI crosses below oversold level
        result.loc[(result['rsi'] < self.oversold) & 
                   (result['rsi'].shift(1) >= self.oversold), 
                   'signal'] = 1
        
        # Sell when RSI crosses above overbought level
        result.loc[(result['rsi'] > self.overbought) & 
                   (result['rsi'].shift(1) <= self.overbought), 
                   'signal'] = -1
        
        self.signals = result
        return result
