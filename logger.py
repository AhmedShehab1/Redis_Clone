#!/usr/bin/env python3
"""Logger Module
"""
import logging
import os


class Logger:

    FILE = os.path.dirname(os.path.abspath(__file__)).split('/')[-1] +  '/application.log'
    FORMATTER = '%(asctime)s-%(name)s-%(levelname)s-%(message)s'


    def __init__(self, name: str, level: int):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter(Logger.FORMATTER)
        file_handler = logging.FileHandler(Logger.FILE)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

