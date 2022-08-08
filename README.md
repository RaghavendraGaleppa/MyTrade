# MyTrade
Trading Library

### 1. Basic usage of the OandaAPI
    
```python
from my_trade.oanda import OandaAPI

api_key = 'your_api_key'
account_id = 'your_account_id'
url = 'https://api-fxpractice.oanda.com/v3/'

oanda = OandaAPI(api_key, account_id, url)
print(oanda.get_price_data(fx='EUR_USD', granularity='M1', count=1))
```

##### Using a credentials_file
A credentials file is a json file with the following structure:

```json
{
    "api_key": "your_api_key",
    "account_id": "your_account_id",
    "url": "https://api-fxpractice.oanda.com/v3/"
}
```

You can load it as follows:
    
```python
from my_trade.oanda import OandaAPI

oanda = OandaAPI.get_oanda_api(credentials_file='credentials.json')
print(oanda.get_price_data(fx='EUR_USD', granularity='M1', count=1))
```



