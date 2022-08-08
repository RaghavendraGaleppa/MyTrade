"""
Handle blocking and async requests
"""
import aiohttp

from my_trade.utils.logging_utils import getLogger

request_utils_logger = getLogger("request_utils", logging_level="DEBUG")
request_utils_logger.debug("Request utils logger initialized")


async def async_get(url, params=None, headers=None):
    """
    Make a GET request
    :param url: url to make the request to
    :param params: params to send with the request
    :param headers: headers to send with the request
    :return: response object
    """
    async with aiohttp.ClientSession() as session:
        request_utils_logger.debug(f"url: {url}")
        request_utils_logger.debug(f"params: {params}")
        request_utils_logger.debug(f"headers: {headers}")
        async with session.get(url, params=params, headers=headers) as response:
            # Check if the response is successful
            if response.status != 200:
                text = await response.text()
                request_utils_logger.error(f"Error: {response.status} {text}")
                return None
            return await response.json()


async def async_post(url, json_data=None, headers=None):
    """
    Make a POST request
    :param url: url to make the request to
    :param json_data: data to send with the request
    :param headers: headers to send with the request
    :return: response object
    """
    async with aiohttp.ClientSession() as session:
        request_utils_logger.debug(f"url: {url}")
        request_utils_logger.debug(f"json_data: {json_data}")
        request_utils_logger.debug(f"headers: {headers}")
        async with session.post(url, json=json_data, headers=headers) as response:
            # Check if the response is successful
            if response.status != 200:
                text = await response.text()
                request_utils_logger.error(f"Error: {response.status} {text}")
                return None
            return await response.json()
