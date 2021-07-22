import logging
import os
import sys


class Logger(object):

    @staticmethod
    def get_logger(module_name: str) -> logging.Logger:
        logger = logging.getLogger(module_name)
        sh = logging.StreamHandler(sys.stdout)
        log_level = os.environ.get('LOG_LEVEL', 'INFO').strip().lower()

        if log_level == 'debug':
            logger.setLevel(logging.DEBUG)
            sh.setLevel(logging.DEBUG)
        elif log_level == 'warning':
            logger.setLevel(logging.WARNING)
            sh.setLevel(logging.WARNING)
        elif log_level == 'error':
            logger.setLevel(logging.ERROR)
            sh.setLevel(logging.ERROR)
        else:
            logger.setLevel(logging.INFO)
            sh.setLevel(logging.INFO)

        log_format = '[%(asctime)s - %(name)s - %(lineno)s - %(funcName)s - %(levelname)s]: %(message)s'
        formatter = logging.Formatter(log_format)
        sh.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(sh)
        return logger
