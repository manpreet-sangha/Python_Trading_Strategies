"""Example: Visualizing strategy results.

Note: If imports fail, install the package in development mode:
    pip install -e .
"""
from strategies.macd_strategy import MACDStrategy
from backtesting.backtest import Backtest
from utils.data_loader import generate_sample_data
from utils.visualizations import (
    plot_price_and_signals,
    plot_portfolio_value,
    plot_strategy_analysis
)
import matplotlib.pyplot as plt


def main():
    """Run MACD strategy with visualization example."""
    print("=" * 60)
    print("MACD Strategy with Visualization Example")
    print("=" * 60)
    
    # Generate sample data
    print("\nGenerating sample data...")
    data = generate_sample_data(start_date='2020-01-01', end_date='2023-12-31')
    print(f"Data shape: {data.shape}")
    
    # Initialize and run strategy
    print("\nInitializing MACD Strategy...")
    strategy = MACDStrategy(fast_period=12, slow_period=26, signal_period=9)
    signals = strategy.generate_signals(data)
    
    # Run backtest
    print("\nRunning backtest...")
    backtest = Backtest(initial_capital=100000, commission=0.001)
    results = backtest.run(signals)
    
    # Print results
    print()
    backtest.print_results()
    
    # Create visualizations
    print("\nGenerating visualizations...")
    
    # Plot 1: Price and signals
    print("  - Creating price and signals chart...")
    plot_price_and_signals(signals, strategy_name="MACD Strategy")
    
    # Plot 2: Portfolio value
    print("  - Creating portfolio value chart...")
    plot_portfolio_value(results)
    
    # Plot 3: Comprehensive analysis
    print("  - Creating comprehensive analysis chart...")
    plot_strategy_analysis(signals, results, strategy_name="MACD Strategy")
    
    print("\nVisualization complete! Close the plot windows to exit.")
    plt.show()


if __name__ == "__main__":
    main()
