import pandas_datareader.data as web
import yfinance as yf
import matplotlib.pyplot as plt
from zipline.api import order, symbol
from zipline.algorithm import TradingAlgorithm

yf.pdr_override()
data = web.get_data_yahoo("AAPL", start="2010-01-01", end="2021-01-01")

data = data[["Close"]]
data.columns = ["APPL"]
data = data.tz_localize("UTC")


def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 1)


algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

plt.plot(result.index, result.portfolio_value)
plt.show()