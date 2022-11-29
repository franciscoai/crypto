# By franciscoaiglesias@gmail.com - 2022
# Insired on:
#        https://blog.devgenius.io/download-and-analyze-crypto-market-data-with-python-c23941e475f

#Load the required libraries
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# list of crptocurrencies as ticker arguments
cryptocurrencies = ['BNB-USD','BTC-USD', 'ETH-USD', 'XRP-USD']


data = yf.download(cryptocurrencies, start='2020-01-01',
                end='2021-12-12')
data.head()

adj_close=data['Adj Close']
adj_close.head()

# ploting the adjusted closing price
fig, axs =plt.subplots(2,2,figsize=(16,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
axs[0,0].plot(adj_close['BNB-USD'])
axs[0,0].set_title('BNB')
axs[0,1].plot(adj_close['BTC-USD'])
axs[0,1].set_title('BTC')
axs[1,0].plot(adj_close['ETH-USD'])
axs[1,0].set_title('ETH')
axs[1,1].plot(adj_close['XRP-USD'])
axs[1,1].set_title('XRP')
plt.show()

# Returns i.e. percentage change in the adjusted close price and drop the first row with NA's
returns = adj_close.pct_change().dropna(axis=0)
#view the first 5 rows of the data frame
returns.head()

# Cumulative return series
cum_returns = ((1 + returns).cumprod() - 1) *100
cum_returns.head()
cum_returns.plot(figsize=(20,6))
plt.title('Cumulative Returns')


#compute the correlations
returns.corr()
#plot the correlations
sns.heatmap(returns.corr(), annot=True, cmap='coolwarm')
plt.show()
