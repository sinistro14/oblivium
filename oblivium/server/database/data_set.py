#!/usr/bin/env python3.6


class DataSet:

    def __init__(self, data_set):
        self.__data_set = data_set

    def get_topics(self):
        topics = "Available topics:\n"
        for i in range(0, len(self.__data_set)):
            data = self.__data_set[i]
            topics += str(i) + '. ' + data.get_topic() + '\n'
        return topics

    def get_number_of_topics(self):
        return len(self.__data_set)

    def get_info(self, index):
        return self.__data_set[index].get_random_info()
