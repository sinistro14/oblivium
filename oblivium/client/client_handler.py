#!/usr/bin/env python3.6

from oblivium.common.security import CryptoHandler, RandomHandler
from oblivium.common.messages import RequestMessage, ConnectionRequest


class ClientHandler:

    """
    Client request handler

    Must override the handle method to implement communication with the server
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
            response = self.receive()  # get ResponseMessage (public key and random messages x_n)
            server_public_key = CryptoHandler.import_key(response.get_public_key())

            # Issue request
            print("Which set do you wish to get information from (0/1) ?\n")

            print("Set 0: {}\n".format(response.get_random_messages()[0]))
            print("Set 1: {}\n".format(response.get_random_messages()[1]))

            print("Type -1 to exit.")
            b = int(input("> "))

            if 0 <= b < response.get_number_of_topics():

                x_b = response.get_random_messages()[b]
                k = RandomHandler.get_random_integer_list(3, 1)[0]

                v = CryptoHandler.calculate_v(x_b, server_public_key.n, server_public_key.e, k)

                self.send(RequestMessage(v))  # send v to client

                obt_message = self.receive()  # get ObtMessage (m'n messages)
                mb = obt_message.get_mn(b)

                print("Received m'0:\n{}\n".format(obt_message.get_mn(0)))
                print("Received m'1:\n{}\n".format(obt_message.get_mn(1)))

                m = CryptoHandler.decrypt_m(mb, k)  # decipher the requested message, m_b

                print("Returned value, with id {}, was:\n{}\n".format(b, m))

                break
            else:
                break
