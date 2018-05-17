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
            server_public_key = response.get_public_key()
            print(server_public_key)
            print(response.get_random_messages)
            print("\n{}".format(response.get_topics()))

            # Issue request
            print("Which set do you wish to get information from ?")
            print("Type -1 to exit")
            b = int(input("> "))
            if 0 <= b < response.get_number_of_topics():

                x_b = response.get_random_messages()[b]  # get random message
                k = RandomHandler.get_random_bytes(sec_constants.NUMBER_OF_RANDOM_BYTES)
                v = CryptoHandler.calculate_v(k, server_public_key, x_b)

                self.send(RequestMessage(v))

                obt_message = self.receive()  # get ObtMessage
                mb = obt_message.get_mn(b)

                print("Received m0: {}".format(obt_message.get_mn(0)))
                print("Received m1: {}".format(obt_message.get_mn(1)))

                m = CryptoHandler.decrypt_m(mb, k)

                print("Return value was:\n{}".format(m))

                break
            else:
                break
