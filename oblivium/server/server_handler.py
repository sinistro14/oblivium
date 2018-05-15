#!/usr/bin/env python3.6

import socketserver

from oblivium.common import sec_constants, network_constants, protocol_settings
from oblivium.common.security import CryptoHandler, RandomHandler
from oblivium.common.messages import ResponseMessage,  SendMessage
from oblivium.server.server_dataset import ServerDataSet
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

                    # prepare RSA key info
                    server_key_pair = CryptoHandler.generate_rsa_key_pair()
                    server_public_key = server_key_pair.publickey()
                    server_private_key = server_key_pair

                    # prepare available data sets
                    data_set = ServerDataSet.get_instance().get_data_set(
                        protocol_settings.DATA_SET_SIZE_VALUE
                    )
                    data_set_topics = data_set.get_topics()
                    m0 = data_set.get_info(0)
                    m1 = data_set.get_info(1)
                    print("Available messages are:\n{}\n{}".format(m0, m1))


                    # generate random bytes list
                    random_messages = RandomHandler.get_random_bytes_list(
                        sec_constants.NUMBER_OF_RANDOM_BYTES,
                        data_set.get_number_of_topics()
                    )

                    # send ResponseMessage
                    self.send(
                        ResponseMessage(
                            server_public_key.exportKey(),
                            data_set_topics,
                            random_messages
                        )
                    )

                    request = self.receive()  # get RequestMessage
                    print("Received {}".format(request.get_v()))  # TODO use v accordingly

                    ml0 = CryptoHandler.amazing_function_1(request.get_v(), server_public_key, server_private_key,
                                                               random_messages[0], m0)
                    ml1 = CryptoHandler.amazing_function_1(request.get_v(), server_public_key, server_private_key,
                                                               random_messages[1], m1)

                    self.send(SendMessage(ml0))
                    self.send(SendMessage(ml1))

                    break
                else:
                    break

        except Exception as e:
            print("Connection with {} {}".format(self.client_address, e))

        print("Closing connection with {}".format(self.client_address))
