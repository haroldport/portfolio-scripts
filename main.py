from PortfolioService import *
from Utilities import *


stocks = list()
stock_cache = dict()


def _print_portfolio():
    print('Portfolio resume')
    print('*' * 50)
    for stock in stocks:
        print(str(stock))
    print('\n')


def _get_or_add_financial_values_to_cache(ticker):
    try:
        financial_in_cache = stock_cache[ticker]
        if financial_in_cache:
            print('Found ticker {0} in cache with beta: {1}'.format(ticker.upper(), financial_in_cache['beta']))
            return financial_in_cache
    except KeyError:
        pass
    try:
        financial_values = PortfolioService.get_financial_values_by_ticker(ticker.upper())
        stock_cache[ticker] = financial_values
        print('Found ticker {0} in Yahoo Finance with beta: {1}'.format(ticker.upper(), financial_values['beta']))
        return financial_values
    except TypeError:
        print('Ticker does not exist')
        return None


def _create_portfolio_with_number_of_actions():
    print('Please enter the portfolio data')
    while True:
        try:
            n = int(input('How many stocks do you want to enter? '))
            i = 1
            while n > 0:
                print('Values for Stock {0}'.format(i))
                ticker = Utilities.create_ticker(stocks)
                financial_values = _get_or_add_financial_values_to_cache(ticker)
                if financial_values:
                    beta = financial_values['beta']
                    number_of_actions = Utilities.create_number_of_actions()
                    stock = PortfolioService.create_stock(ticker, 0, number_of_actions,
                                                          beta, financial_values['current_price'])
                    stocks.append(stock)
                    n -= 1
                    i += 1
            break
        except ValueError:
            print('Please enter a number')
    _print_portfolio()


def _create_portfolio_with_percentage():
    print('Please enter the portfolio data')
    while True:
        try:
            n = int(input('How many stocks do you want to enter? '))
            total_iterations = n
            i = 1
            total_percentage = 0
            while n > 0:
                print('Values for Stock {0}'.format(i))
                ticker = Utilities.create_ticker(stocks)
                financial_values = _get_or_add_financial_values_to_cache(ticker)
                if financial_values:
                    while True:
                        percentage = Utilities.create_percentage()
                        total_percentage += percentage
                        if total_percentage > 100:
                            total_percentage -= percentage
                            print('Sum of percentages exceeded')
                        elif i == total_iterations and total_percentage < 100:
                            total_percentage -= percentage
                            print('Sum of percentages must be 100%')
                        else:
                            stock = PortfolioService.create_stock(ticker, percentage, 0, financial_values['beta'],
                                                                  financial_values['current_price'])
                            stocks.append(stock)
                            n -= 1
                            i += 1
                            break
            break
        except ValueError:
            print('Please enter a number')
    _print_portfolio()


def _menu_options():
    stocks.clear()
    print('\n')
    print('*' * 50)
    print('Portfolio Management')
    print('*' * 50)
    print('Enter option to calculate')
    print('[B] - Beta Portfolio')
    print('[S] - Standard Deviation and Sharpe Ratio')
    print('[E] - Exit')


if __name__ == '__main__':
    _menu_options()

    command = 'A'
    while True:
        command = input()
        command = command.upper()

        if command == 'B':
            _create_portfolio_with_percentage()
            portfolio_beta = PortfolioService.calculate_portfolio_beta(stocks)
            print('Beta Portfolio: {0}'.format(portfolio_beta))
        elif command == 'S':
            _create_portfolio_with_number_of_actions()
            deviation_tuple = PortfolioService.calculate_annual_standard_deviation(stocks)
            sharpe_ratio = PortfolioService.calculate_sharpe_ratio(deviation_tuple)
            print('\n')
            print('Standard deviation: {0}%'.format(round(deviation_tuple[0], 2)))
            print('Annualized Standard deviation: {0}%'.format(round(deviation_tuple[1], 2)))
            print('\n')
            print('Sharpe ratio: {0}%'.format(sharpe_ratio))
        elif command == 'E':
            break
        else:
            print('Invalid command')
        _menu_options()
