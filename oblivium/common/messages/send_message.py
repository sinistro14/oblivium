#!/usr/bin/env python3.6


class SendMessage:
    """
    Message sent by the client to the server, v = (x'b + k^e) mod N
    """
    __k0 = None

    def __init__(self, k0):
        self.__k0 = k0

    def get_k0(self):
        return self.__k0
