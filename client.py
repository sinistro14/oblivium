#!/usr/bin/env python3.6

import socket

from oblivium.client import Client
from oblivium.client.exceptions import ClientSocketException, ClientTimeoutException
from oblivium.common.network import constants

# Echo client program


def main():

    with socket.socket(constants.SOCKET_AF, constants.SOCKET_TYPE) as sock:

        sock.settimeout(constants.CLIENT_HANDLER_TIMEOUT)

        try:
            sock.connect((constants.SERVER_HOST, constants.SERVER_PORT))
        except socket.error as e:
            print("Client: could not establish connection to server - {}".format(e.args[1]))
            exit(1)

        try:
            # blocking call
            Client(sock).handle()
        except ClientTimeoutException as e:
            print("Client: connection to server timed out - {}".format(e.args[1]))
        except ClientSocketException as e:
            print("Client: socket error - {}".format(e.args[1]))

        sock.close()
        print("Client: connection was closed")

    exit(0)


if __name__ == '__main__':
    main()
