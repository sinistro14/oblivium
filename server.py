#!/usr/bin/env python3.6

from oblivium.common.network import constants
from oblivium.server import Server, ServerHandler

# Echo server program


def main():

    server_host, server_port = constants.SERVER_HOST, constants.SERVER_PORT

    server = Server((server_host, server_port), ServerHandler)

    server.start()

    print("Server: server was shutdown")

    exit(0)


if __name__ == "__main__":
    main()
