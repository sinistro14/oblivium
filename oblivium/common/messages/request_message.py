#!/usr/bin/env python3.6


class RequestMessage:
    """
    Message sent by the client to the server, v = (x'b + k^e) mod N
    """
    __v = None

    def __init__(self, v):
        self.__v = v

    def get_v(self):
        return self.__v
