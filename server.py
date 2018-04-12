#!/usr/bin/env python3.6

from oblivium.common.network import constants
from oblivium.server import Server, ServerHandler
from oblivium.cmd import ServerCmd

# Echo server program


def main():

    server = Server((constants.SERVER_HOST, constants.SERVER_PORT), ServerHandler)

    ServerCmd(server)

    exit(0)


if __name__ == "__main__":
    main()
