

import logging


class LogBuilder:
    _logger = logging.getLogger(__name__)

    @staticmethod
    def set_log_level(log_level=logging.INFO):
        LogBuilder._logger.setLevel(log_level)
        return LogBuilder

    @staticmethod
    def enable_stdout():
        LogBuilder._logger.addHandler(logging.StreamHandler())
        return LogBuilder

    @staticmethod
    def get():
        return LogBuilder._logger
