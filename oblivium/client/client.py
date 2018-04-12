#!/usr/bin/env python3.6

import socket

from oblivium.common.network import constants
from oblivium.client.client_handler import ClientHandler
from oblivium.common.network.network_utils import string_to_base64, base64_to_string
from oblivium.client.exceptions import ClientSocketException, ClientTimeoutException


class Client:

    """
    Client
    Establishes connection to server
    """

    def __init__(self):
        self.__sock = socket.socket(constants.SOCKET_AF, constants.SOCKET_TYPE)
        self.__sock.settimeout(constants.CLIENT_HANDLER_TIMEOUT)  # timeout
        self.__client_handler = ClientHandler(self)

    def start(self):
        try:
            self.__sock.connect((constants.SERVER_HOST, constants.SERVER_PORT))
        except socket.error as e:
            print("Client: could not establish connection to server - {}".format(e.args[1]))
            exit(1)

        try:
            # blocking call
            self.__handle()
        except ClientTimeoutException as e:
            print("Client: connection to server timed out - {}".format(e.args[1]))
        except ClientSocketException as e:
            print("Client: socket error - {}".format(e.args[1]))

    def __handle(self):
        try:
            self.__client_handler.handle()
        except Exception as e:
            raise e

    def stop(self):
        self.__sock.close()
        print("Client: connection to server was closed")

    # should only be used by handler
    def send(self, data):
        try:
            self.__sock.sendall(string_to_base64(data))
        except socket.timeout as e:
            raise ClientTimeoutException(e.args)
        except socket.error as e:
            raise ClientSocketException(e.args)

    # should only be used by handler
    def receive(self):
        try:
            data = str(base64_to_string(self.__sock.recv(constants.BYTES_TO_READ)))
            if data:
                return data
            else:
                raise ClientSocketException("", "connection was lost")
        except socket.timeout as e:
            raise ClientTimeoutException(e.args)
        except socket.error as e:
            raise ClientSocketException(e.args)
