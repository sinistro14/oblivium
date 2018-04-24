#!/usr/bin/env python3.6

from oblivium.server.database import Data, DataSet
from oblivium.common.protocol import DATA_SET_FILE_PATH, DATA_SET_FILE_ACCESS


class ServerDataSet:

    # Only available instance
    __instance = None

    @staticmethod
    def get_instance():
        if ServerDataSet.__instance is None:
            ServerDataSet.__instance = ServerDataSet()  # initiate data set
        return ServerDataSet.__instance

    def __init__(self):
        self.__load_data_set()

    def __load_data_set(self):
        data = {}  # will map each topic to its information
        topic_marker = "[TOPIC]"
        with open(DATA_SET_FILE_PATH, DATA_SET_FILE_ACCESS) as data_set:
            topic = ""
            topics = []
            info = []
            for line in data_set:
                line = line.rstrip()  # removes /n or /r
                if line:
                    if line.startswith(topic_marker):
                        if info:
                            data[topic] = Data(topic, info)   # save info block
                            topics.append(topic)
                            info = []                         # restart info gatherer
                        topic = ' '.join(line.split()[1:])  # get only what comes after topic marker
                    else:
                        info.append(line)
            if topic and info:  # catch the last topic info, upon file exit
                data[topic] = Data(topic, info)
                topics.append(topic)
        self.__topics = topics
        self.__data_set = data

    def get_data_set(self, data_set_size):
        data_set = []
        if data_set_size <= len(self.__data_set):  # will return empty list, otherwise
            for i in range(0, data_set_size):
                topic = self.__topics[i]
                data_set.append(self.__data_set[topic])
        return DataSet(data_set)
