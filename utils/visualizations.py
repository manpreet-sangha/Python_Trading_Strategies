"""Visualization utilities for trading strategies."""
import matplotlib.pyplot as plt
import pandas as pd
from typing import Optional


def plot_price_and_signals(data: pd.DataFrame, strategy_name: str = "Strategy",
                           save_path: Optional[str] = None):
    """Plot price chart with buy/sell signals.
    
    Args:
        data: DataFrame with 'Close' prices and 'signal' column
        strategy_name: Name of the strategy for the plot title
        save_path: Optional path to save the plot
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Plot closing price
    ax.plot(data.index, data['Close'], label='Close Price', linewidth=1.5)
    
    # Plot buy signals
    buy_signals = data[data['signal'] == 1]
    ax.scatter(buy_signals.index, buy_signals['Close'], 
              color='green', marker='^', s=100, label='Buy Signal', zorder=5)
    
    # Plot sell signals
    sell_signals = data[data['signal'] == -1]
    ax.scatter(sell_signals.index, sell_signals['Close'],
              color='red', marker='v', s=100, label='Sell Signal', zorder=5)
    
    ax.set_title(f'{strategy_name} - Price and Signals', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price', fontsize=12)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_portfolio_value(backtest_results: dict, save_path: Optional[str] = None):
    """Plot portfolio value over time.
    
    Args:
        backtest_results: Results dictionary from Backtest.run()
        save_path: Optional path to save the plot
    """
    data = backtest_results['data']
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Plot portfolio value
    ax.plot(data.index, data['portfolio_value'], 
           label='Portfolio Value', linewidth=2, color='blue')
    
    # Add horizontal line for initial capital
    ax.axhline(y=backtest_results['initial_capital'], 
              color='gray', linestyle='--', label='Initial Capital', alpha=0.7)
    
    ax.set_title('Portfolio Value Over Time', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Portfolio Value ($)', fontsize=12)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    
    # Format y-axis as currency
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_strategy_analysis(data: pd.DataFrame, backtest_results: dict,
                           strategy_name: str = "Strategy",
                           save_path: Optional[str] = None):
    """Create a comprehensive analysis plot with multiple subplots.
    
    Args:
        data: DataFrame with strategy signals
        backtest_results: Results dictionary from Backtest.run()
        strategy_name: Name of the strategy
        save_path: Optional path to save the plot
    """
    fig, axes = plt.subplots(3, 1, figsize=(14, 12))
    
    # Subplot 1: Price and signals
    ax1 = axes[0]
    ax1.plot(data.index, data['Close'], label='Close Price', linewidth=1.5)
    
    buy_signals = data[data['signal'] == 1]
    ax1.scatter(buy_signals.index, buy_signals['Close'],
               color='green', marker='^', s=100, label='Buy Signal', zorder=5)
    
    sell_signals = data[data['signal'] == -1]
    ax1.scatter(sell_signals.index, sell_signals['Close'],
               color='red', marker='v', s=100, label='Sell Signal', zorder=5)
    
    ax1.set_title(f'{strategy_name} - Price and Signals', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Price', fontsize=10)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Portfolio value
    ax2 = axes[1]
    backtest_data = backtest_results['data']
    ax2.plot(backtest_data.index, backtest_data['portfolio_value'],
            label='Portfolio Value', linewidth=2, color='blue')
    ax2.axhline(y=backtest_results['initial_capital'],
               color='gray', linestyle='--', label='Initial Capital', alpha=0.7)
    
    ax2.set_title('Portfolio Value Over Time', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Portfolio Value ($)', fontsize=10)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # Subplot 3: Cumulative returns
    ax3 = axes[2]
    ax3.plot(backtest_data.index, backtest_data['cumulative_returns'] * 100,
            label='Cumulative Returns', linewidth=2, color='green')
    ax3.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
    
    ax3.set_title('Cumulative Returns', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Date', fontsize=10)
    ax3.set_ylabel('Returns (%)', fontsize=10)
    ax3.legend(loc='best')
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_indicator(data: pd.DataFrame, indicator_column: str,
                  title: str = "Technical Indicator",
                  save_path: Optional[str] = None):
    """Plot a technical indicator.
    
    Args:
        data: DataFrame containing the indicator
        indicator_column: Name of the column to plot
        title: Title for the plot
        save_path: Optional path to save the plot
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), 
                                    gridspec_kw={'height_ratios': [2, 1]})
    
    # Plot price
    ax1.plot(data.index, data['Close'], label='Close Price', linewidth=1.5)
    ax1.set_title(title, fontsize=14, fontweight='bold')
    ax1.set_ylabel('Price', fontsize=12)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    # Plot indicator
    ax2.plot(data.index, data[indicator_column], 
            label=indicator_column, linewidth=1.5, color='orange')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel(indicator_column, fontsize=12)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig
