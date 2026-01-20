"""Base strategy class for all trading strategies."""
from abc import ABC, abstractmethod
import pandas as pd


class BaseStrategy(ABC):
    """Base class for all trading strategies.
    
    All trading strategies should inherit from this class and implement
    the generate_signals method.
    """
    
    def __init__(self, name: str):
        """Initialize the strategy.
        
        Args:
            name: Name of the strategy
        """
        self.name = name
        self.signals = None
        
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate trading signals based on the strategy rules.
        
        Args:
            data: DataFrame with OHLCV data (Open, High, Low, Close, Volume)
                  Must have DatetimeIndex
        
        Returns:
            DataFrame with added 'signal' column where:
                1 = Buy signal
                -1 = Sell signal
                0 = Hold/No signal
        """
        pass
    
    def __str__(self):
        """String representation of the strategy."""
        return f"{self.name} Strategy"
