from os import system, name


class Utilities:
    @staticmethod
    def clear():
        if name == 'nt':
            _ = system('cls')

        else:
            _ = system('clear')

    @staticmethod
    def create_ticker(stocks):
        while True:
            ticker = input('Enter ticker: ')
            stock_filtered = list(filter(lambda x: x.ticker == ticker, stocks))
            if ticker.strip() and len(stock_filtered) == 0:
                break
            print('Empty or repeated value. Try again')
        return ticker

    @staticmethod
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

    @staticmethod
    def create_number_of_actions():
        while True:
            try:
                actions = int(input('Enter number of actions: '))
                break
            except ValueError:
                print('Try again')
        return actions
