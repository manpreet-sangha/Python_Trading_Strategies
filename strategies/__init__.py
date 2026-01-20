"""Trading strategies module."""
from .base_strategy import BaseStrategy
from .ma_crossover import MovingAverageCrossover
from .rsi_strategy import RSIStrategy
from .macd_strategy import MACDStrategy

__all__ = [
    'BaseStrategy',
    'MovingAverageCrossover',
    'RSIStrategy',
    'MACDStrategy'
]
