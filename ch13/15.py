import pandas_datareader.data as web
import matplotlib.pyplot as plt

h = web.DataReader('005380.KS', 'yahoo')  # 현대자동차

ma5 = h['Close'].rolling(window=5).mean()
ma20 = h['Close'].rolling(window=20).mean()
ma60 = h['Close'].rolling(window=60).mean()
ma120 = h['Close'].rolling(window=120).mean()

h["MA5"] = ma5
h["MA20"] = ma20
h["MA60"] = ma60
h["MA120"] = ma120

plt.plot(h.index, h["Close"], label="Close")
plt.plot(h.index, h["MA5"], label="MA5")
plt.plot(h.index, h["MA20"], label="MA20")
plt.plot(h.index, h["MA60"], label="MA60")
plt.plot(h.index, h["MA120"], label="MA120")

h.info()

plt.legend(loc='best')
plt.grid()
plt.show()


