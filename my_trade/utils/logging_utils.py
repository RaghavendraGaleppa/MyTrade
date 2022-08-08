"""
Handle logging based utils
"""
import logging
import sys


def getLogger(name, logging_level="DEBUG", logging_file=None):
    """
    Get a logger object
    :param name: name of the logger
    :param logging_level: logging level
    :param logging_file: logging file
    :return: logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    # create a file handler
    if logging_file is not None:
        handler = logging.FileHandler(logging_file)
    else:
        handler = logging.StreamHandler(stream=sys.stdout)

    # Add error handler as well
    error_handler = logging.StreamHandler(stream=sys.stderr)
    error_handler.setLevel(logging.ERROR)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(error_handler)

    return logger

