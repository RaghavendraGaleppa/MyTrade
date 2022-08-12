import requests
import json
import pandas as pd

from urllib.parse import urljoin
from my_trade.utils.logging_utils import getLogger
from my_trade.utils.request_utils import async_get

oanda_logger = getLogger("oanda", logging_level="DEBUG")
oanda_logger.debug("Oanda logger initialized")


class OandaAPI:

    def __init__(self, api_token, account_id, url):
        self.api_token = api_token
        self.account_id = account_id
        self.url = url

    def get_price_data(self, fx="EUR_USD", granularity="M1", count=10):
        url = urljoin(self.url, f"/v3/instruments/{fx}/candles")
        oanda_logger.debug(f"url: {url}")

        params = {
            'granularity': granularity,
            'count': count
        }
        headers = {
            'Authorization': f'Bearer {self.api_token}'
        }
        response = requests.get(url, params=params, headers=headers)

        if response.status_code != 200:
            oanda_logger.error(f"Error: {response.status_code}")
            oanda_logger.error(f"{response.text}")
            return None

        return response.json()

    async def async_get_price_data(self, fx="EUR_USD", granularity="M1", count=10, return_type="json"):
        url = urljoin(self.url, f"/v3/instruments/{fx}/candles")
        oanda_logger.debug(f"url: {url}")

        params = {
            'granularity': granularity,
            'count': count
        }
        headers = {
            'Authorization': f'Bearer {self.api_token}'
        }
        response = await async_get(url, params=params, headers=headers)

        if response is None:
            return None

        if return_type == "json":
            return response

        elif return_type == "dataframe":
            candles = []
            for candle in response['candles']:
                ohlc_data = {
                    'date_time': candle['time'],
                    'open': candle['mid']['o'],
                    'high': candle['mid']['h'],
                    'low': candle['mid']['l'],
                    'close': candle['mid']['c'],
                    'volume': candle['volume'],
                    'complete': candle['complete']
                }
                candles.append(ohlc_data)

            # Convert to pandas dataframe
            df = pd.DataFrame(candles)
            # date_time field is in utc, convert it to DatetimeIndex
            df['date_time'] = pd.to_datetime(df['date_time'])
            df.set_index('date_time', inplace=True)
            return df

        else:
            raise ValueError(f"Invalid return_type: {return_type}. It must be 'json' or 'dataframe'")

    @classmethod
    def get_oanda_api(cls, credentials_file=None, api_token=None, account_id=None, url=None):
        if credentials_file is not None:
            with open(credentials_file, "r") as f:
                # It is a json file
                credentials = json.load(f)
                api_token = credentials.get("api_token")
                account_id = credentials.get("account_id")
                url = credentials.get("url")

        if api_token is None or account_id is None or url is None:
            raise Exception("Missing credentials")

        return cls(api_token, account_id, url)
