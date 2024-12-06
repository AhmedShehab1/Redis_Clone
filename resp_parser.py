#!/usr/bin/env python3
"""RESP Parser Module
"""
import re


class RESPParser:
    def parse_bulk_string(self, input_string):

        pattern = r"\$[0-9]+\r\n(.+?)\r\n"
        matches = re.findall(pattern, input_string)
        if not matches:
            raise ValueError("Invalid RESP Format")

        command = matches[0]
        args = matches[1:]
        return command, args
