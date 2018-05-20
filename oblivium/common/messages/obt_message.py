#!/usr/bin/env python3.6


class ObtMessage:
    """
    Message sent by the server to the client,
    with list [m'0, m'1, ..., m'n], where m'n = m_n + ( (v - x_b)^d mod N )
    """
    __m_list = None

    def __init__(self, m_list=()):
        self.__m_list = list(m_list)  # convert tuple to list

    def add_m(self, m):
        self.__m_list.append(m)

    def add_mn(self, position, m):
        self.__m_list.insert(position, m)

    def get_mn(self, position):
        return self.__m_list[position]
