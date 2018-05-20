#!/usr/bin/env python3.6

import secrets
import random
from Crypto import Random
from oblivium.common.security import constants
from math import gcd


class RandomHandler:

    @staticmethod
    def get_random_bytes_generator():
        """
        Provides a random generator
        :return: random generator
        """
        return Random.new().read

    @staticmethod
    def generate_random():
        """
        Generates a random integer
        :return: random integer
        """
        return random.randrange(constants.MAX_GENERATION_LIMIT)

    @staticmethod
    def get_random_integers(modulo, number_of_values=1):
        """
        Random integer generator

        :param modulo: modulo of the values to generate
        :param number_of_values: number of integers to generate
        :return: returns an iterable integer generator
        """
        count = 0
        while count < number_of_values:
            a = int(round(RandomHandler.generate_random() % modulo))
            while gcd(a, modulo) != 1:
                a = int(round(RandomHandler.generate_random() % modulo))
            yield a
            count += 1

    @staticmethod
    def get_random_integer_list(modulo, list_size):
        """
        Returns random integer list

        :param modulo: modulo of the values to generate
        :param list_size: number of integers to generate
        :return: random integer list
        """
        list_of_integers = []
        for i in RandomHandler.get_random_integers(modulo, list_size):
            list_of_integers.append(i)
        return list_of_integers
