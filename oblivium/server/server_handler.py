#!/usr/bin/env python3.6

import socketserver

from oblivium.common import sec_constants, network_constants, protocol_settings
from oblivium.common.security import CryptoHandler, RandomHandler
from oblivium.common.messages import ResponseMessage,  ObtMessage
from oblivium.common.network import object_to_base64, base64_to_object


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
        return base64_to_object(self.request.recv(network_constants.BYTES_TO_READ))

    def handle(self):
        # self.request is the TCP socket connected to the client
        # defines N seconds timeout
        self.request.settimeout(network_constants.SERVER_HANDLER_TIMEOUT)

        try:
            while True:

                # presentation
                data = self.receive()  # get ConnectionRequest
                if data:
                    # handle presentation request
                    print("Connection established with {}".format(self.client_address))

                    number_of_topics = 2

                    # prepare RSA key info
                    server_key_pair = CryptoHandler.generate_rsa_key_pair()
                    server_public_key = server_key_pair.publickey()
                    server_private_key = server_key_pair
                    base_modulus = server_public_key.n

                    #generate number_of_topics messages to be sent

                    ms = RandomHandler.get_random_integer_list(base_modulus, number_of_topics)

                    m0 = ms[0]
                    m1 = ms[1]
                    print("Available messages are:\n0. {}\n1. {}".format(m0, m1))

                    # generate random int list
                    random_messages = RandomHandler.get_random_integer_list(
                        base_modulus,
                        number_of_topics
                    )
                    print("Random messages:\n{}".format(random_messages))

                    # send ResponseMessage
                    self.send(
                        ResponseMessage(
                            server_public_key.exportKey(),
                            random_messages
                        )
                    )

                    request = self.receive()  # get RequestMessage (v)

                    v = request.get_v()

                    print("Received v:\n{}".format(v))

                    obt_message = ObtMessage()

                    #generate number_of_topics m's
                    for i in range(0, number_of_topics):
                        obt_message.add_m(
                            CryptoHandler.encrypt_m(v, server_public_key,
                                                    server_private_key, random_messages[i], ms[i])
                        )
                    #send m's to the client
                    self.send(obt_message)
                    print("Finished communicating with client {}".format(self.client_address))

                    break
                else:
                    break

        except Exception as e:
            print("Connection with {} - Error {}".format(self.client_address, e))

        print("Closing connection with {}".format(self.client_address))
