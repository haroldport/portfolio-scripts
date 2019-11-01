from os import system, name

from PortfolioService import *


stocks = list()
stock_cache = list()


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def _create_ticker():
    while True:
        ticker = input('Enter ticker: ')
        stock_filtered = list(filter(lambda x: x.ticker == ticker, stocks))
        if ticker.strip() and len(stock_filtered) == 0:
            break
        print('Empty or repeated value. Try again')
    return ticker


def create_percentage():
    while True:
        try:
            percentage = int(input('Enter percentage: '))
            if 0 <= percentage <= 100:
                break
            print('Try again')
        except ValueError:
            print('Try again')
    return percentage


def _print_portfolio():
    print('Portfolio resume')
    print('*' * 50)
    for stock in stocks:
        print(str(stock))
    print('\n')


def _portfolio_data():
    print('Portfolio Management')
    print('*' * 50)
    print('Please enter the portfolio data')
    try:
        n = int(input('How many stocks do you want to enter? '))
        total_iterations = n
        i = 1
        total_percentage = 0
        while n > 0:
            print('Values for Stock {0}'.format(i))
            ticker = _create_ticker()
            try:
                beta = PortfolioService.calculate_beta_by_ticker(ticker.upper())
                print('Found ticker {0} with beta: {1}'.format(ticker.upper(), beta))
                while True:
                    percentage = create_percentage()
                    total_percentage += percentage
                    if total_percentage > 100:
                        total_percentage -= percentage
                        print('Sum of percentages exceeded')
                    elif i == total_iterations and total_percentage < 100:
                        total_percentage -= percentage
                        print('Sum of percentages must be 100%')
                    else:
                        stock = PortfolioService.create_stock(ticker, percentage, beta, stock_cache)
                        stocks.append(stock)
                        stock_cache.append(stock)
                        n -= 1
                        i += 1
                        break
            except TypeError:
                print('Ticker does not exist')
    except ValueError:
        print('Please enter a number')

    _print_portfolio()


def _menu_options():
    print('Enter option to calculate')
    print('[P] - Portfolio Beta')
    print('[S] - Standard Deviation')
    print('[R] - Sharpie Ratio')


def _submenu_options():
    print('\n')
    print('[E] - Exit, Or select another option to calculate')


if __name__ == '__main__':
    _portfolio_data()
    _menu_options()

    command = 'A'
    while True:
        command = input()
        command = command.upper()

        if command == 'P':
            portfolio_beta = PortfolioService.calculate_portfolio_beta(stocks)
            print('\n')
            print('Portfolio Beta: {0}'.format(portfolio_beta))
        elif command == 'S':
            print('Standard Deviation')
        elif command == 'R':
            print('Sharpie Ratio')
        elif command == 'E':
            break
        else:
            print('Invalid command')
        _submenu_options()
