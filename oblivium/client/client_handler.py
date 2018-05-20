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
            response = self.receive()  # get ResponseMessage (public key and random messages)
            server_public_key = CryptoHandler.import_key(response.get_public_key()) #get the public key

            # Issue request
            print("Which set do you wish to get information from (0/1) ?") #choose on of two sets represented with
                                                                           # random integers
            print("Set 0: ",  response.get_random_messages()[0])
            print("Set 1: ", response.get_random_messages()[1])

            print("Type -1 to exit.")
            b = int(input("> "))
            if 0 <= b < response.get_number_of_topics():

                x_b = response.get_random_messages()[b]  # get random message
                k = RandomHandler.get_random_integer_list(3, 1)[0] # 1 or 2 (chosed randomly)
                v = CryptoHandler.calculate_v(k, server_public_key, x_b) #v= (x_b + k^e) mod N

                self.send(RequestMessage(v)) #send v

                obt_message = self.receive()  # get ObtMessage
                mb = obt_message.get_mn(b) #get m's

                print("Received m'0: {}\n".format(obt_message.get_mn(0)))
                print("Received m'1: {}\n".format(obt_message.get_mn(1)))

                m = CryptoHandler.decrypt_m(mb, k) #get the b(0 or 1) original message

                print("Returned value, with id {}, was:\n{}".format(b, m))

                break
            else:
                break
