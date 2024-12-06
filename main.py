#!/usr/bin/env python3
"""Entry Point
"""
import os
from .server import RedisServer
import argparse


def main():
    parser = argparse.ArgumentParser(description="Redis Clone")
    basedir = os.path.abspath(os.path.dirname(__file__))
    parser.add_argument("--dir", default=basedir, help=f"Directory for Redis files (default: {basedir}).")
    parser.add_argument("--dbfilename", default="dump.rdb", help="Name of Redis dump file (default: dump.rdb).")

    args = parser.parse_args()

    redis_server = RedisServer(host="localhost", port=6379, directory=args.dir, dbfilename=args.dbfilename)
    redis_server.start()

if __name__ == "__main__":
    main()