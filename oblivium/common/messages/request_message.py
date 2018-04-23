#!/usr/bin/env python3.6


class InitialMessage:

    __public_key = None
    __number_of_messages = 2
    __random_messages = []

    def __init__(self, public_key, number_of_messages, random_messages):
        self.__public_key = public_key
        self.__number_of_messages = number_of_messages
        self.__random_messages = random_messages

    def get_public_key(self):
        return self.__public_key

    def get_number_of_messages(self):
        return self.__number_of_messages

    def get_random_messages(self):
        return self.__random_messages
