#!/usr/bin/env python3.6


class InitialMessage:

    __string = ""

    def __init__(self, string):
        self.__string = string

    def get_string(self):
        return self.__string
