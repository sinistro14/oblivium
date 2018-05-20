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
    def generate_random(): #generate a random integer
        return random.randrange(constants.MAX_GENERATION_LIMIT)

    @staticmethod
    def get_random_integers(modulo, number_of_values=1): #generate a random integer module modulo and prime with modulo
        count = 0
        while count < number_of_values:
            a = int(round(RandomHandler.generate_random() % modulo))
            while gcd(a, modulo) != 1:
                a = int(round(RandomHandler.generate_random() % modulo))
            yield a
            count += 1

    @staticmethod
    def get_random_integer_list(mod, list_size): #create a list with get_random_integers
        list_of_integers = []
        for i in RandomHandler.get_random_integers(mod, list_size):
            list_of_integers.append(i)
        return list_of_integers
