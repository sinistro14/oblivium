#!/usr/bin/env python3.6

import signal


class ServerController:

    def __init__(self, server):
        self.__server = server
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

    def exit(self, signum, frame):
        self.__server.stop()
