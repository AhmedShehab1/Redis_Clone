#!/usr/bin/env python3
"""Server Module
"""

import socket
import threading
from .command_handler import CommandHandler
from .resp_parser import RESPParser
from .logger import Logger
import logging
import os


class RedisServer:
    def __init__(self, directory, dbfilename, host="localhost", port=6379):
        if directory and not os.path.exists(directory):
            raise ValueError(f"Directory '{directory}' does not exist.")
        if directory and not os.path.isdir(directory):
            raise ValueError(f"'{directory}' is not a valid directory.")

        self.directory = directory
        self.dbfilename = dbfilename
        self.host = host
        self.port = port
        self.server_socket = socket.create_server((host, port), reuse_port=True)
        self.command_handler = CommandHandler(directory, dbfilename)
        self.logger = Logger(name="Redis Server", level=logging.INFO).logger

    def start(self):
        print(f"Starting Redis clone on {self.host}:{self.port}")
        self.logger.info(f"Starting Redis clone on {self.host}:{self.port}")

        while True:
            client_socket, _ = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            thread.start()

    def handle_client(self, client_socket):
        parser = RESPParser()
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break

                command, args = parser.parse_bulk_string(data.decode())
                response = self.command_handler.execute(command, args)
                client_socket.sendall(response.encode())
        except Exception as e:
            client_socket.sendall(b"-ERROR\r\n")
        finally:
            client_socket.close()
