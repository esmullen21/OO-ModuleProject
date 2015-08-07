class CurrencyRate:
    """This class is for storing information of the curreny rate. The currecny
    name, currency code and the conversion rate to euro are stored as attributes"""

    def __init__(self, currencyName, currencyCode, rateToEuro):
        self.currencyName=currencyName
        self.currencyCode=currencyCode
        self.rateToEuro=rateToEuro


