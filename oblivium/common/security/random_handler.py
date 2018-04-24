#!/usr/bin/env python3.6

import secrets
from Crypto import Random


class RandomHandler:

    @staticmethod
    def get_random_generator():
        return Random.new().read

    @staticmethod
    def get_random_bytes(number_of_bytes):
        return secrets.token_bytes(number_of_bytes)

    @staticmethod
    def get_random_bytes_list(number_of_bytes, list_size):
        list_of_bytes = []
        for i in range(0, list_size):
            list_of_bytes.append(RandomHandler.get_random_bytes(number_of_bytes))
        return list_of_bytes
