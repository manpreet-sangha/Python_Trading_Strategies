"""Example: Running an RSI strategy with backtesting.

Note: If imports fail, install the package in development mode:
    pip install -e .
"""
from strategies.rsi_strategy import RSIStrategy
from backtesting.backtest import Backtest
from utils.data_loader import generate_sample_data


def main():
    """Run RSI strategy example."""
    print("=" * 60)
    print("RSI Trading Strategy Example")
    print("=" * 60)
    
    # Generate sample data
    print("\nGenerating sample data...")
    data = generate_sample_data(start_date='2020-01-01', end_date='2023-12-31')
    print(f"Data shape: {data.shape}")
    print(f"Date range: {data.index[0]} to {data.index[-1]}")
    
    # Initialize strategy
    print("\nInitializing RSI Strategy...")
    strategy = RSIStrategy(period=14, oversold=30, overbought=70)
    print(f"RSI Period: 14")
    print(f"Oversold Level: 30")
    print(f"Overbought Level: 70")
    
    # Generate signals
    print("\nGenerating trading signals...")
    signals = strategy.generate_signals(data)
    buy_signals = (signals['signal'] == 1).sum()
    sell_signals = (signals['signal'] == -1).sum()
    print(f"Buy signals: {buy_signals}")
    print(f"Sell signals: {sell_signals}")
    
    # Run backtest
    print("\nRunning backtest...")
    backtest = Backtest(initial_capital=100000, commission=0.001)
    results = backtest.run(signals)
    
    # Print results
    print()
    backtest.print_results()


if __name__ == "__main__":
    main()
