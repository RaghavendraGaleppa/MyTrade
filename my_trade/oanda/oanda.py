import requests

from urllib.parse import urljoin
from my_trade.utils.logging_utils import getLogger
from my_trade.utils.request_utils import async_get, async_post

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

    async def async_get_price_data(self, fx="EUR_USD", granularity="M1", count=10):
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
            oanda_logger.error(f"Error: {response.status_code}")
            oanda_logger.error(f"{response.text}")
            return None

        return response
