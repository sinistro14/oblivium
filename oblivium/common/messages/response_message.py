#!/usr/bin/env python3.6


class ResponseMessage:
    """
    Represents the initial Server message, where the available data
    is presented to the client, as well as the server's public key
    and the set of random messages to be used, as required by the
    protocol
    """

    __public_key = None
    __random_messages = []

    def __init__(self, public_key, random_messages):
        self.__public_key = public_key
        self.__random_messages = random_messages

    def get_public_key(self):
        return self.__public_key

    def get_number_of_topics(self):
        return len(self.__random_messages)

    def get_random_messages(self):
        return self.__random_messages
