# application to dev in Fintual
# Manuel Olivares
# Date: 09/03/2022 
from datetime import *
class Portfolio:
    def __init__(self):
        self.stocks = {}
    def add_stock(self,date_,price):
        """ Enter Date in 'DD/MM/YYYY' format."""
        date_ = date(int(str(date_).split("/")[2]),int(str(date_).split("/")[1]),int(str(date_).split("/")[0]))
        self.stocks[date_] = price
    def get_price(self,date_):
        """ Enter Date in 'DD/MM/YYYY' format."""
        date_ = date(int(str(date_).split("/")[2]),int(str(date_).split("/")[1]),int(str(date_).split("/")[0]))
        return self.stocks[date_]
    def profit(self,date_start,date_end):
        """ Enter Date in 'DD/MM/YYYY' format."""
        return self.get_price(date_end) - self.get_price(date_start)
portfolio = Portfolio()
tmp = portfolio.add_stock("01/01/2021",800)
tmp = portfolio.add_stock("31/12/2021",801)
annualized_return = f" The annualized return of portfolio is: ${portfolio.profit('01/01/2021','31/12/2021')}"
print(annualized_return)
        