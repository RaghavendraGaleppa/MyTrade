from my_trade.oanda import OandaAPI

import json

oanda = OandaAPI.get_oanda_api(credentials_file='credentials.json')

df = oanda.get_price_data('EUR_USD', count=1000, return_type="dataframe")

# Add a stochastic oscillator (SO) column to the dataframe
df['so'] = df['close'].rolling(window=14).mean() / df['close'].rolling(window=14).std() * 100
print(df.tail())


