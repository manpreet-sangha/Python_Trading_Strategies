"""Backtesting framework for trading strategies."""
import pandas as pd


class Backtest:
    """Simple backtesting framework for trading strategies."""
    
    def __init__(self, initial_capital: float = 100000, commission: float = 0.001):
        """Initialize the backtester.
        
        Args:
            initial_capital: Starting capital for backtesting (default: 100000)
            commission: Commission per trade as a fraction (default: 0.001 = 0.1%)
        """
        self.initial_capital = initial_capital
        self.commission = commission
        self.results = None
        
    def run(self, strategy_data: pd.DataFrame) -> dict:
        """Run backtest on strategy signals.
        
        Args:
            strategy_data: DataFrame with 'Close' prices and 'signal' column
        
        Returns:
            Dictionary containing backtest results and performance metrics
        """
        data = strategy_data.copy()
        
        # Initialize positions and portfolio value
        data['position'] = 0
        data['portfolio_value'] = float(self.initial_capital)
        
        current_position = 0
        cash = self.initial_capital
        shares = 0
        
        for i in range(len(data)):
            signal = data['signal'].iloc[i]
            price = data['Close'].iloc[i]
            
            # Execute trades based on signals
            if signal == 1 and current_position == 0:  # Buy signal
                # Buy with all available cash
                shares = cash / (price * (1 + self.commission))
                cash = 0
                current_position = 1
                
            elif signal == -1 and current_position == 1:  # Sell signal
                # Sell all shares
                cash = shares * price * (1 - self.commission)
                shares = 0
                current_position = 0
            
            # Update position and portfolio value
            data.loc[data.index[i], 'position'] = current_position
            data.loc[data.index[i], 'portfolio_value'] = cash + (shares * price)
        
        # Calculate returns
        data['returns'] = data['portfolio_value'].pct_change()
        data['cumulative_returns'] = (1 + data['returns']).cumprod() - 1
        
        # Calculate performance metrics
        total_return = (data['portfolio_value'].iloc[-1] - self.initial_capital) / self.initial_capital
        
        # Count trades
        trades = (data['signal'] != 0).sum()
        
        # Calculate max drawdown
        rolling_max = data['portfolio_value'].expanding().max()
        drawdown = (data['portfolio_value'] - rolling_max) / rolling_max
        max_drawdown = drawdown.min()
        
        results = {
            'initial_capital': self.initial_capital,
            'final_value': data['portfolio_value'].iloc[-1],
            'total_return': total_return,
            'total_return_pct': total_return * 100,
            'num_trades': trades,
            'max_drawdown': max_drawdown,
            'max_drawdown_pct': max_drawdown * 100,
            'data': data
        }
        
        self.results = results
        return results
    
    def print_results(self):
        """Print backtest results in a readable format."""
        if self.results is None:
            print("No backtest results available. Run backtest first.")
            return
        
        print("=" * 50)
        print("BACKTEST RESULTS")
        print("=" * 50)
        print(f"Initial Capital: ${self.results['initial_capital']:,.2f}")
        print(f"Final Value: ${self.results['final_value']:,.2f}")
        print(f"Total Return: {self.results['total_return_pct']:.2f}%")
        print(f"Number of Trades: {self.results['num_trades']}")
        print(f"Max Drawdown: {self.results['max_drawdown_pct']:.2f}%")
        print("=" * 50)
