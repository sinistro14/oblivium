#!/usr/bin/env python3.6

import socket

from oblivium.common.network import constants
from oblivium.client.client_handler import ClientHandler
from oblivium.common.network.network_utils import string_to_base64, base64_to_string
from oblivium.client.exceptions import ClientSocketException, ClientTimeoutException


class Client:

    def __init__(self, sock):
        self.__sock = sock
        self.__client_handler = ClientHandler(self)

    def send(self, data):
        try:
            self.__sock.sendall(string_to_base64(data))
        except socket.timeout as e:
            raise ClientTimeoutException(e.args)
        except socket.error as e:
            raise ClientSocketException(e.args)

    def receive(self):
        try:
            data = str(base64_to_string(self.__sock.recv(constants.BYTES_TO_READ)))
            if data:
                return data
            else:
                raise ClientSocketException("", "connection was lost.")
        except socket.timeout as e:
            raise ClientTimeoutException(e.args)
        except socket.error as e:
            raise ClientSocketException(e.args)

    def handle(self):
        try:
            self.__client_handler.handle()
        except Exception as e:
            raise e
