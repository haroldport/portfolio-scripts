from datetime import date, timedelta
from math import sqrt

from yahoofinancials import YahooFinancials
import numpy as np

from Stock import Stock


class PortfolioService:
    """Service to management Portfolio"""

    @staticmethod
    def _print_ending():
        print('\n')
        print('-' * 50)
        print('\n')

    @staticmethod
    def _get_and_print_time_period():
        today = date.today()
        three_years_ago = today - timedelta(days=(3 * 365))
        print('\nTime period: {0} / {1}'.format(three_years_ago, today))
        return {'start_date': three_years_ago, 'end_date': today}

    @staticmethod
    def _get_historical_price_data(ticker, start_date, end_date):
        s = YahooFinancials(ticker)
        historical_data = s.get_historical_price_data(str(start_date), str(end_date), "daily")
        return historical_data[ticker.upper()]['prices']

    @staticmethod
    def get_financial_values_by_ticker(ticker):
        print('Finding ticker in Yahoo Finance...')
        s = YahooFinancials(ticker)
        financial_values = {'beta': round(s.get_beta(), 2), 'current_price': round(s.get_current_price(), 2),
                            'prev_close_price': round(s.get_prev_close_price(), 2)}
        return financial_values

    @staticmethod
    def calculate_portfolio_beta(portfolio_data):
        percentage_by_beta = list(map(lambda x: (x.percentage / 100) * x.beta, portfolio_data))
        return round(sum(percentage_by_beta), 2)

    @staticmethod
    def _merge_prices(ticker_prices):
        merge_prices = dict()
        for key in ticker_prices:
            for k, v in [(k, v) for x in ticker_prices[key] for (k, v) in x.items()]:
                merge_prices.setdefault(k, []).append(v)
        return merge_prices

    @staticmethod
    def _calculate_daily_return(merge_prices, stocks_weight):
        portfolio_daily_return = list()
        first_key = list(merge_prices.keys())[0]
        prev_price = merge_prices[first_key]
        for price_key in merge_prices:
            current_price = merge_prices[price_key]
            if first_key == price_key:
                continue
            total_daily_return = 0
            for i in range(len(current_price)):
                for j in range(len(prev_price)):
                    if i == j:
                        stock_daily_return = ((current_price[i]/prev_price[j]) - 1) * 100
                        total_daily_return += stock_daily_return * stocks_weight[j]
            portfolio_daily_return.append(total_daily_return/100)
            prev_price = current_price
        deviation = np.std(portfolio_daily_return)
        annualized_deviation = deviation * sqrt(252)
        return deviation, annualized_deviation

    @staticmethod
    def calculate_annual_standard_deviation(portfolio_data):
        print('\nCalculating annualized standard deviation...')
        total_portfolio = sum(list(map(lambda x: x.number_of_actions * x.price, portfolio_data)))
        stocks_weight = list()
        ticker_prices = dict()
        time_period = PortfolioService._get_and_print_time_period()
        print('\nStocks weight')
        for stock in portfolio_data:
            weight = ((stock.number_of_actions * stock.price) * 100) / total_portfolio
            print('{0}: {1}'.format(stock.ticker.upper(), round(weight, 2)))
            stocks_weight.append(round(weight, 2))
            prices_by_ticker = PortfolioService._get_historical_price_data(stock.ticker, time_period['start_date'],
                                                                           time_period['end_date'])
            ticker_prices[stock.ticker] = list(map(lambda x: {x['formatted_date']: round(x['close'], 2)},
                                                   prices_by_ticker))
        merge_prices = PortfolioService._merge_prices(ticker_prices)
        return PortfolioService._calculate_daily_return(merge_prices, stocks_weight)

    @staticmethod
    def create_stock(ticker, percentage, number_of_actions, beta, price):
        stock = Stock(ticker, percentage, number_of_actions, beta, price)
        PortfolioService._print_ending()
        return stock
