#!/usr/bin/env python3.6

import signal


class ServerController:
    """
    Server Signal detector
    Ensures server proper cleanup upon CTRL-C receiver
    """

    def __init__(self, server):
        self.__server = server
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

    def exit(self, signum, frame):
        """Exits cmd, after proper cleanup"""
        self.__server.stop()
