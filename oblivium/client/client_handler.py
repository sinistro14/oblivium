#!/usr/bin/env python3.6

from oblivium.common import sec_constants
from oblivium.common.security import CryptoHandler, RandomHandler
from oblivium.common.messages import RequestMessage, ConnectionRequest

class ClientHandler:

    """
    The request handler class for our client

    Must override the handle method to implement communication with the
    server
    """

    def __init__(self, client):
        self.__client = client

    def send(self, data):
        self.__client.send(data)

    def receive(self):
        return self.__client.receive()

    def handle(self):

        while True:

            # Establish connection to server
            self.send(ConnectionRequest())
            response = self.receive()  # get ResponseMessage
            server_public_key = CryptoHandler.import_key(response.get_public_key())

            # Issue request
            print("Which set do you wish to get information from (0/1) ?")
            print("Type -1 to exit.")
            b = int(input("> "))
            if 0 <= b < response.get_number_of_topics():

                x_b = response.get_random_messages()[b]  # get random message
                k = RandomHandler.get_random_integers(3).__next__()
                v = CryptoHandler.calculate_v(k, server_public_key, x_b)

                self.send(RequestMessage(v))

                obt_message = self.receive()  # get ObtMessage
                mb = obt_message.get_mn(b)

                print("Received m'0: {}\n".format(obt_message.get_mn(0)))
                print("Received m'1: {}\n".format(obt_message.get_mn(1)))

                m = CryptoHandler.decrypt_m(mb, k)

                print("Returned value, with id {}, was:\n{}".format(b, m))

                break
            else:
                break
