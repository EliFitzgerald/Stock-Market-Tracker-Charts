#This opens Yahoo Finance data set library
import yfinance as yf
# This pulls Histroical FInance for Apple from Yahoo Finance
ticker = yf.Ticker("AAPL")
# Fetches 1 year of daily data (Open, High, Low, Close)
data = ticker.history(period="1y")
# Calculates thw 20 - day Simple Move Average (SMA)
# This smooths out short-term fluctuations and shows the average closing price over 20 days and 50 days
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# matplotlib is used for plotting graphs
import matplotlib.pyplot as plt
# sets the size of chart wha
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA_20'], label='20-Day SMA')
plt.plot(data['SMA_50'], label='50-Day SMA')
# Adds a Legend To Chart
plt.legend()
# Adds a title to the chart
plt.title("AAPL Price & Moving Averages")
# Displays the Chart
plt.show()
