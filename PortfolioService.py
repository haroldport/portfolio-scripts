from yahoofinancials import YahooFinancials

from Stock import Stock


class PortfolioService:
    """Service to management Portfolio"""

    @staticmethod
    def _print_ending():
        print('\n')
        print('-' * 50)
        print('\n')

    @staticmethod
    def calculate_beta_by_ticker(ticker):
        print('Finding ticker in Yahoo Finance...')
        s = YahooFinancials(ticker)
        return round(s.get_beta(), 2)

    @staticmethod
    def calculate_portfolio_beta(portfolio_data):
        percentage_by_beta = list(map(lambda x: (x.percentage/100) * x.beta, portfolio_data))
        return round(sum(percentage_by_beta), 2)

    @staticmethod
    def create_stock(ticker, percentage, beta, stock_cache):
        stock_filtered = list(filter(lambda x: x.ticker == ticker, stock_cache))
        if len(stock_filtered) > 0:
            s = stock_filtered[0]
            PortfolioService._print_ending()
            return s
        stock = Stock(ticker, percentage, beta)
        PortfolioService._print_ending()
        return stock
