"""Example: Running a Moving Average Crossover strategy with backtesting."""
import sys
sys.path.append('..')

from strategies.ma_crossover import MovingAverageCrossover
from backtesting.backtest import Backtest
from utils.data_loader import generate_sample_data


def main():
    """Run Moving Average Crossover strategy example."""
    print("=" * 60)
    print("Moving Average Crossover Strategy Example")
    print("=" * 60)
    
    # Generate sample data
    print("\nGenerating sample data...")
    data = generate_sample_data(start_date='2020-01-01', end_date='2023-12-31')
    print(f"Data shape: {data.shape}")
    print(f"Date range: {data.index[0]} to {data.index[-1]}")
    
    # Initialize strategy
    print("\nInitializing Moving Average Crossover Strategy...")
    strategy = MovingAverageCrossover(short_period=50, long_period=200)
    print(f"Short MA Period: 50")
    print(f"Long MA Period: 200")
    
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
