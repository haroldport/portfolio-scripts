class Stock:
    def __init__(self, ticker, percentage, beta=0):
        self.ticker = ticker
        self.percentage = percentage
        self.beta = beta

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
    def beta(self):
        return self._beta

    @beta.setter
    def beta(self, beta):
        self._beta = beta

    def __str__(self):
        return 'Stock: ticker={0}, percentage={1}, beta={2}'.format(self.ticker.upper(), self.percentage, self.beta)

    def __repr__(self):
        return 'Stock({0}, {1}, {2})'.format(self.ticker.upper(), self.percentage, self.beta)
