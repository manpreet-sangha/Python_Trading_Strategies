# Python Trading Strategies

A comprehensive repository for researching, exploring, and implementing systematic rule-based trading strategies deployed by traders in the capital markets.

## Overview

This repository provides a framework for developing and backtesting algorithmic trading strategies using Python. It includes:

- **Technical Indicators**: Common indicators like SMA, EMA, RSI, MACD, and Bollinger Bands
- **Trading Strategies**: Pre-built strategies including Moving Average Crossover, RSI, and MACD strategies
- **Backtesting Framework**: Simple but effective backtesting engine to evaluate strategy performance
- **Extensible Architecture**: Easy-to-extend base classes for creating custom strategies

## Project Structure

```
Python_Trading_Strategies/
├── strategies/          # Trading strategy implementations
│   ├── base_strategy.py      # Base class for all strategies
│   ├── ma_crossover.py       # Moving Average Crossover strategy
│   ├── rsi_strategy.py       # RSI-based strategy
│   └── macd_strategy.py      # MACD-based strategy
├── indicators/          # Technical indicator implementations
│   ├── moving_averages.py    # SMA and EMA indicators
│   ├── momentum.py           # RSI and MACD indicators
│   └── volatility.py         # Bollinger Bands
├── backtesting/         # Backtesting framework
│   └── backtest.py           # Main backtesting engine
├── utils/              # Utility functions
│   └── data_loader.py        # Data loading and generation utilities
├── examples/           # Example usage scripts
│   ├── example_ma_crossover.py
│   ├── example_rsi_strategy.py
│   └── example_macd_strategy.py
└── data/               # Directory for market data files
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/manpreet-sangha/Python_Trading_Strategies.git
cd Python_Trading_Strategies
```

2. Install the package in development mode (recommended):
```bash
pip install -e .
```

Or install required dependencies directly:
```bash
pip install -r requirements.txt
```

## Quick Start

### Running Example Strategies

Run the example scripts to see the strategies in action:

```bash
cd examples
python example_ma_crossover.py
python example_rsi_strategy.py
python example_macd_strategy.py
```

### Using the Framework

Here's a simple example of how to use the framework:

```python
from strategies.rsi_strategy import RSIStrategy
from backtesting.backtest import Backtest
from utils.data_loader import generate_sample_data

# Generate sample data
data = generate_sample_data(start_date='2020-01-01', end_date='2023-12-31')

# Initialize strategy
strategy = RSIStrategy(period=14, oversold=30, overbought=70)

# Generate signals
signals = strategy.generate_signals(data)

# Run backtest
backtest = Backtest(initial_capital=100000, commission=0.001)
results = backtest.run(signals)
backtest.print_results()
```

## Available Strategies

### 1. Moving Average Crossover
Generates buy signals when short-term MA crosses above long-term MA, and sell signals when it crosses below.

**Parameters:**
- `short_period`: Period for short-term moving average (default: 50)
- `long_period`: Period for long-term moving average (default: 200)

### 2. RSI Strategy
Generates buy signals when RSI crosses below oversold threshold, and sell signals when it crosses above overbought threshold.

**Parameters:**
- `period`: RSI calculation period (default: 14)
- `oversold`: Oversold threshold (default: 30)
- `overbought`: Overbought threshold (default: 70)

### 3. MACD Strategy
Generates buy signals when MACD line crosses above signal line, and sell signals when it crosses below.

**Parameters:**
- `fast_period`: Fast EMA period (default: 12)
- `slow_period`: Slow EMA period (default: 26)
- `signal_period`: Signal line period (default: 9)

## Creating Custom Strategies

To create your own strategy, inherit from the `BaseStrategy` class:

```python
from strategies.base_strategy import BaseStrategy
import pandas as pd

class MyCustomStrategy(BaseStrategy):
    def __init__(self):
        super().__init__("My Custom Strategy")
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        result = data.copy()
        result['signal'] = 0
        
        # Implement your strategy logic here
        # Set result['signal'] to:
        #   1 for buy signals
        #  -1 for sell signals
        #   0 for hold/no signal
        
        return result
```

## Technical Indicators

The repository includes the following technical indicators:

### Moving Averages
- **SMA (Simple Moving Average)**: `indicators.moving_averages.sma(data, period)`
- **EMA (Exponential Moving Average)**: `indicators.moving_averages.ema(data, period)`

### Momentum Indicators
- **RSI (Relative Strength Index)**: `indicators.momentum.rsi(data, period)`
- **MACD**: `indicators.momentum.macd(data, fast_period, slow_period, signal_period)`

### Volatility Indicators
- **Bollinger Bands**: `indicators.volatility.bollinger_bands(data, period, num_std)`

## Backtesting

The backtesting framework provides:
- Position tracking
- Commission calculation
- Performance metrics (total return, max drawdown, number of trades)
- Portfolio value tracking over time

```python
from backtesting.backtest import Backtest

backtest = Backtest(initial_capital=100000, commission=0.001)
results = backtest.run(strategy_signals)
backtest.print_results()
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- New trading strategies
- Additional technical indicators
- Improved backtesting features
- Bug fixes and optimizations
- Documentation improvements

## Disclaimer

This repository is for educational and research purposes only. The strategies and indicators provided should not be used for live trading without thorough testing and understanding. Past performance does not guarantee future results. Always do your own research and consider consulting with financial professionals before making investment decisions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
