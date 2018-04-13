#!/usr/bin/env python3.6

import socketserver

from oblivium.common.network import constants
from oblivium.common.messages import ResponseMessage
from oblivium.common.network.network_utils import object_to_base64, base64_to_object


class ServerHandler(socketserver.BaseRequestHandler):

    """
    The request handler class for our server

    It is instantiated once per connection to the server, and must
    override the handle method to implement communication to the
    client
    """

    def send(self, data):
        self.request.sendall(object_to_base64(data))

    def receive(self):
        return base64_to_object(self.request.recv(constants.BYTES_TO_READ))

    def handle(self):

        # defines N seconds timeout
        self.request.settimeout(constants.SERVER_HANDLER_TIMEOUT)

        try:
            while True:
                # self.request is the TCP socket connected to the client
                data = self.receive()  # get InitialMessage
                if data:
                    print("{} wrote:".format(self.client_address))
                    string = data.get_string()
                    print(string)
                    # just send back the same data, but upper-cased
                    self.send(ResponseMessage(string.upper()))
                else:
                    break
        except Exception as e:
            print("Connection with {} {}".format(self.client_address, e))

        print("Closing connection with {}".format(self.client_address))
