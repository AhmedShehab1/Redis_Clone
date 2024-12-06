#!/usr/bin/env python3
"""Command Handler Module
"""
from functools import wraps
import time

def manage_expiry(get_method):
    @wraps(get_method)
    def wrapper(command_handler, key):
        key = key[0]
        current_time = int(time.time() * 1000)
        if key in command_handler.dictionary:
            entry = command_handler.dictionary[key]
            if entry['expiry_time'] and current_time > entry['expiry_time']:
                command_handler.dictionary.pop(key)

        return get_method(command_handler, key)
    return wrapper

class CommandHandler:
    def __init__(self, dir, dbfilename):
        self.dictionary = {}
        self.dir = dir
        self.dbfilename = dbfilename

    def execute(self, command, args):
        method = getattr(self, command.lower(), None)
        if not method:
            return f"-ERROR: Unknown command {command}\r\n"
        return method(args)

    def ping(self, args=None):
        return "+PONG\r\n"

    def echo(self, args):
        return f'${len(args[0])}\r\n{args[0]}\r\n'

    def set(self, args):
        key, val = args[:2]

        if len(args) > 3 and args[2].upper() == 'PX':
            expiry = int(args[3])
            expiry_time = int(time.time() * 1000) + expiry
        else:
            expiry_time = None

        self.dictionary[key] = {'value': val, 'expiry_time': expiry_time}
        return "+OK\r\n"

    @manage_expiry
    def get(self, key):
        entry = self.dictionary.get(key)
        if entry is None:
            return "$-1\r\n"
        value = entry['value']
        return f"${len(value)}\r\n{value}\r\n"

    def config(self, args):
        if args[0].upper() == 'GET':
            key = args[1]
            val = getattr(self, key)
            return f"*2\r\n${len(key)}\r\n{key}\r\n${len(val)}\r\n{val}\r\n"