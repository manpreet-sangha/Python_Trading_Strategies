# Strategy Documentation

This document provides detailed information about the trading strategies implemented in this repository.

## Table of Contents
1. [Moving Average Crossover Strategy](#moving-average-crossover-strategy)
2. [RSI Strategy](#rsi-strategy)
3. [MACD Strategy](#macd-strategy)
4. [Creating Custom Strategies](#creating-custom-strategies)

---

## Moving Average Crossover Strategy

### Overview
The Moving Average Crossover strategy is one of the most popular and simple trend-following strategies. It uses two moving averages - a short-term and a long-term - to identify trend changes.

### How It Works
- **Buy Signal**: Generated when the short-term moving average crosses above the long-term moving average (Golden Cross)
- **Sell Signal**: Generated when the short-term moving average crosses below the long-term moving average (Death Cross)

### Parameters
- `short_period`: Period for the short-term moving average (default: 50 days)
- `long_period`: Period for the long-term moving average (default: 200 days)

### Best Use Cases
- Trending markets
- Long-term investment strategies
- Markets with clear directional movements

### Limitations
- Generates false signals in sideways/choppy markets
- Lag in signal generation (due to moving average calculation)
- May miss quick reversals

### Example Usage
```python
from strategies.ma_crossover import MovingAverageCrossover

strategy = MovingAverageCrossover(short_period=50, long_period=200)
signals = strategy.generate_signals(data)
```

---

## RSI Strategy

### Overview
The Relative Strength Index (RSI) strategy is a momentum-based strategy that identifies overbought and oversold conditions in the market.

### How It Works
- **Buy Signal**: Generated when RSI crosses below the oversold threshold (typically 30), indicating a potential buying opportunity
- **Sell Signal**: Generated when RSI crosses above the overbought threshold (typically 70), indicating a potential selling opportunity

### Parameters
- `period`: Number of periods for RSI calculation (default: 14)
- `oversold`: Oversold threshold level (default: 30)
- `overbought`: Overbought threshold level (default: 70)

### Best Use Cases
- Range-bound markets
- Mean reversion strategies
- Markets with clear support and resistance levels

### Limitations
- Can remain in overbought/oversold territory for extended periods in strong trends
- May generate premature signals in trending markets
- Requires confirmation from other indicators

### Example Usage
```python
from strategies.rsi_strategy import RSIStrategy

strategy = RSIStrategy(period=14, oversold=30, overbought=70)
signals = strategy.generate_signals(data)
```

---

## MACD Strategy

### Overview
The Moving Average Convergence Divergence (MACD) strategy is a trend-following momentum indicator that shows the relationship between two moving averages.

### How It Works
- **Buy Signal**: Generated when the MACD line crosses above the signal line
- **Sell Signal**: Generated when the MACD line crosses below the signal line

### Parameters
- `fast_period`: Fast EMA period (default: 12)
- `slow_period`: Slow EMA period (default: 26)
- `signal_period`: Signal line EMA period (default: 9)

### Best Use Cases
- Trending markets
- Momentum trading
- Identifying trend reversals

### Limitations
- Lag in signal generation
- May generate false signals in sideways markets
- Works best with other confirmation indicators

### Example Usage
```python
from strategies.macd_strategy import MACDStrategy

strategy = MACDStrategy(fast_period=12, slow_period=26, signal_period=9)
signals = strategy.generate_signals(data)
```

---

## Creating Custom Strategies

### Step 1: Inherit from BaseStrategy

All strategies should inherit from the `BaseStrategy` class:

```python
from strategies.base_strategy import BaseStrategy
import pandas as pd

class MyCustomStrategy(BaseStrategy):
    def __init__(self, param1, param2):
        super().__init__("My Custom Strategy Name")
        self.param1 = param1
        self.param2 = param2
```

### Step 2: Implement generate_signals Method

The `generate_signals` method must be implemented:

```python
def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
    """Generate trading signals.
    
    Args:
        data: DataFrame with OHLCV data (Open, High, Low, Close, Volume)
    
    Returns:
        DataFrame with added 'signal' column where:
            1 = Buy signal
            -1 = Sell signal
            0 = Hold/No signal
    """
    result = data.copy()
    result['signal'] = 0
    
    # Implement your strategy logic here
    # Calculate indicators
    # Generate buy/sell signals
    
    return result
```

### Step 3: Use Technical Indicators

You can use any of the built-in indicators:

```python
from indicators.moving_averages import sma, ema
from indicators.momentum import rsi, macd
from indicators.volatility import bollinger_bands

def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
    result = data.copy()
    
    # Calculate indicators
    result['sma_50'] = sma(result['Close'], 50)
    result['rsi'] = rsi(result['Close'], 14)
    bb = bollinger_bands(result['Close'], 20)
    
    # Generate signals based on your rules
    result['signal'] = 0
    # Your logic here...
    
    return result
```

### Step 4: Test Your Strategy

Use the backtesting framework to test your strategy:

```python
from backtesting.backtest import Backtest
from utils.data_loader import generate_sample_data

# Load or generate data
data = generate_sample_data()

# Run strategy
strategy = MyCustomStrategy(param1=value1, param2=value2)
signals = strategy.generate_signals(data)

# Backtest
backtest = Backtest(initial_capital=100000, commission=0.001)
results = backtest.run(signals)
backtest.print_results()
```

---

## Strategy Combination and Optimization

### Combining Multiple Strategies

You can combine signals from multiple strategies:

```python
# Run multiple strategies
ma_signals = ma_strategy.generate_signals(data)
rsi_signals = rsi_strategy.generate_signals(data)

# Combine signals (example: both must agree)
combined = data.copy()
combined['signal'] = 0
combined.loc[(ma_signals['signal'] == 1) & (rsi_signals['signal'] == 1), 'signal'] = 1
combined.loc[(ma_signals['signal'] == -1) & (rsi_signals['signal'] == -1), 'signal'] = -1
```

### Parameter Optimization

Test different parameter combinations to find optimal settings:

```python
best_return = -float('inf')
best_params = None

for short in range(20, 100, 10):
    for long in range(100, 300, 50):
        strategy = MovingAverageCrossover(short_period=short, long_period=long)
        signals = strategy.generate_signals(data)
        backtest = Backtest()
        results = backtest.run(signals)
        
        if results['total_return'] > best_return:
            best_return = results['total_return']
            best_params = (short, long)

print(f"Best parameters: Short={best_params[0]}, Long={best_params[1]}")
print(f"Best return: {best_return:.2%}")
```

---

## Risk Management

Always implement proper risk management:

1. **Position Sizing**: Don't risk more than 1-2% of capital per trade
2. **Stop Losses**: Set maximum loss thresholds
3. **Take Profits**: Define profit targets
4. **Diversification**: Don't put all capital in one strategy or asset
5. **Backtesting**: Test strategies on historical data before live trading

---

## Disclaimer

These strategies are for educational purposes only. Past performance does not guarantee future results. Always conduct thorough research and testing before deploying any trading strategy with real capital.
