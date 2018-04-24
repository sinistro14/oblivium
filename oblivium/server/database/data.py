#!/usr/bin/env python3.6

from random import randint


class Data:

    """
    Information is expected to be a list of strings
    """
    def __init__(self, topic, information):
        self.__topic = topic
        self.__information = information

    def get_topic(self):
        return self.__topic

    def get_data_size(self):
        return len(self.__information)

    def get_random_info(self):
        return self.__information[randint(0, self.get_data_size())]
