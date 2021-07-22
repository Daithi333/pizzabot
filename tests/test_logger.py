import os
import unittest

from pizzabot.logger import Logger


class TestLogger(unittest.TestCase):

    def test_logger_set_at_info_level_when_env_var_not_set(self):
        logger = Logger.get_logger('test_logger')
        self.assertEqual(logger.level, 20)

    def test_logger_set_at_info_level_when_env_var_invalid(self):
        os.environ['LOG_LEVEL'] = 'INVALID'
        logger = Logger.get_logger('test_logger')
        self.assertEqual(logger.level, 20)

    def test_logger_set_at_debug_level_from_env_var(self):
        os.environ['LOG_LEVEL'] = 'DEBUG'
        logger = Logger.get_logger('test_logger')
        self.assertEqual(logger.level, 10)

    def test_logger_set_at_warning_level_from_env_var(self):
        os.environ['LOG_LEVEL'] = 'WARNING'
        logger = Logger.get_logger('test_logger')
        self.assertEqual(logger.level, 30)

    def test_logger_set_at_error_level_from_env_var(self):
        os.environ['LOG_LEVEL'] = 'ERROR'
        logger = Logger.get_logger('test_logger')
        self.assertEqual(logger.level, 40)
