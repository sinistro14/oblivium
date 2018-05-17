#!/usr/bin/env python3.6

import secrets
import random
from Crypto import Random
from oblivium.common.security import constants
from math import gcd


class RandomHandler:

    @staticmethod
    def get_random_bytes_generator():
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

    @staticmethod
    def generate_random():
        return random.randrange(constants.MAX_GENERATION_LIMIT)

    @staticmethod
    def get_random_integers(modulo, number_of_values=1):
        count = 0
        while count < number_of_values:
            a = int(round(RandomHandler.generate_random() % modulo))  # FIXME is this ok?
            while gcd(a, modulo) != 1:
                a = int(round(RandomHandler.generate_random() % modulo))  # FIXME is this ok?
            yield a
            count += 1

    @staticmethod
    def get_random_integer_list(mod, list_size):
        list_of_integers = []
        for i in RandomHandler.get_random_integers(mod, list_size):
            list_of_integers.append(i)
        return list_of_integers
