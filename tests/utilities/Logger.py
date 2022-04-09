import inspect
import logging
import os

from from_root import from_root


def Logger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler(
        os.path.join(os.path.dirname(from_root('tests')), "info.log"), "w")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    # logger.debug("Debug this")
    # logger.info("Info")
    # logger.warning("This is a warning")
    # logger.error("This is a error")
    # logger.critical("This is a critical")
    return logger


Logger()


def currentMethod():
    return os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
