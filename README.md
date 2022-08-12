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

##### Async usage

```python
from my_trade.oanda import OandaAPI

oanda = OandaAPI.get_oanda_api(credentials_file='credentials.json')
df = await oanda.async_get_price_data(fx='EUR_USD', granularity='M1', count=10, return_type='dataframe')
print(df)
```
Output: 

```
date_time                    open     high      low    close  volume  complete
2022-08-12 16:49:00+00:00  1.02577  1.02610  1.02574  1.02608     118      True
2022-08-12 16:50:00+00:00  1.02607  1.02609  1.02594  1.02606      75      True
2022-08-12 16:51:00+00:00  1.02607  1.02613  1.02603  1.02610      34      True
2022-08-12 16:52:00+00:00  1.02610  1.02610  1.02593  1.02598      59      True
2022-08-12 16:53:00+00:00  1.02597  1.02600  1.02582  1.02585      76      True
2022-08-12 16:54:00+00:00  1.02586  1.02588  1.02556  1.02558      90      True
2022-08-12 16:55:00+00:00  1.02561  1.02572  1.02561  1.02568      49      True
2022-08-12 16:56:00+00:00  1.02570  1.02572  1.02553  1.02562      69      True
2022-08-12 16:57:00+00:00  1.02562  1.02572  1.02554  1.02572      58      True
2022-08-12 16:58:00+00:00  1.02574  1.02580  1.02568  1.02574      18     False
```



