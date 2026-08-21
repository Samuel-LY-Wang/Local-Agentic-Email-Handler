"""
We create one logger to use throughout the app.
The logger called "logger" should be used for ALL logging. Do not use any other logger.
"""

import logging

class Log():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def log(self, to_log: str):
        self.logger.info(to_log)

    def warn(self, to_warn: str):
        self.logger.warning(to_warn)

    def error(self, to_error: str):
        self.logger.error(to_error)

logger = Log()