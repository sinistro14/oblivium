#!/usr/bin/env python3.6

import socketserver

from oblivium.common.network import constants
from oblivium.common.network.network_utils import string_to_base64, base64_to_string


class ServerHandler(socketserver.BaseRequestHandler):

    """
    The request handler class for our server

    It is instantiated once per connection to the server, and must
    override the handle method to implement communication to the
    client
    """

    def send(self, data):
        self.request.sendall(string_to_base64(data))

    def receive(self):
        return base64_to_string(self.request.recv(constants.BYTES_TO_READ))

    def handle(self):

        # defines N seconds timeout
        self.request.settimeout(constants.SERVER_HANDLER_TIMEOUT)

        try:
            while True:
                # self.request is the TCP socket connected to the client
                data = self.receive()
                if data:
                    print("{} wrote:".format(self.client_address))
                    print(data)
                    # just send back the same data, but upper-cased
                    self.send(data.upper())
                else:
                    break
        except Exception as e:
            print("Connection with {} {}".format(self.client_address, e))

        print("Closing connection with {}".format(self.client_address))
