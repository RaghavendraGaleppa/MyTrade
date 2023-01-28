"""
A channel basically refers to a python class whose responsibility is to get stock price from a particular source.
This source can be a file or a REST Api endpoint or any other python package as well
"""
import concurrent

from concurrent.futures import ThreadPoolExecutor
from my_trade.oanda import OandaAPI
from my_trade.utils.logging_utils import getLogger

channel_logger = getLogger("channel", logging_level="DEBUG")
channel_logger.debug("Channel logger initialized")


class StockDataLoader:

    def __init__(self, oanda_api: OandaAPI):
        self.oanda_api = oanda_api

    def get_forex_data(self, fx_symbols, granularity="M1", count=10, return_type="json", max_workers=10):
        """
        Get stock price data from Oanda API
        :param fx_symbols: list of forex symbols
        :param granularity: granularity of the data
        :param count: number of candles to get
        :param return_type: return type of the data
        :param max_workers: number of workers to use for the request
        :return: data in the format specified by return_type
        """
        results = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.oanda_api.get_price_data, fx, granularity, count, return_type): fx
                for fx in fx_symbols
            }

            for future in concurrent.futures.as_completed(futures):
                fx = futures[future]
                try:
                    data = future.result()
                    results[fx] = data
                except Exception as e:
                    channel_logger.error(f"Error:{fx}, {e}", exc_info=True)
                    continue

        return results
