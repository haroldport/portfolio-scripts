class Stock:
    def __init__(self, ticker, percentage=0, number_of_actions=0, beta=0, price=0):
        self.ticker = ticker
        self.percentage = percentage
        self.number_of_actions = number_of_actions
        self.beta = beta
        self.price = price

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        self._ticker = ticker

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def number_of_actions(self):
        return self._number_of_actions

    @number_of_actions.setter
    def number_of_actions(self, number_of_actions):
        self._number_of_actions = number_of_actions

    @property
    def beta(self):
        return self._beta

    @beta.setter
    def beta(self, beta):
        self._beta = beta

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return 'Stock: ticker={0}, beta={1}, close price={2}'\
            .format(self.ticker.upper(), self.beta, self.price)

    def __repr__(self):
        return 'Stock({0}, {1}, {2})'.format(self.ticker.upper(), self.percentage, self.beta)
