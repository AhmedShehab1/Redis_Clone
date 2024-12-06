#!/usr/bin/env python3
import socket

def send_redis_command(command, host="localhost", port=6379):
    with socket.create_connection((host, port)) as sock:
        sock.sendall(command.encode())
        response = sock.recv(1024)
        return response.decode()

print("{!r}".format(send_redis_command("*2\r\n$4\r\nECHO\r\n$3\r\nhey\r\n", port=8001)))
print("{!r}".format(send_redis_command("*2\r\n$4\r\nGET\r\n$3\r\nkey\r\n", port=8001)))
print("{!r}".format(send_redis_command("*2\r\n$4\r\nSET\r\n$3\r\nkey\r\n$4\r\nvalue\r\n", port=8001)))
print("{!r}".format(send_redis_command("*2\r\n$4\r\nGET\r\n$3\r\nkey\r\n", port=8001)))
print("{!r}".format(send_redis_command("*1\r\n$4\r\nPING\r\n", port=8001)))