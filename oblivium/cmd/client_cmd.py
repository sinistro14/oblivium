#!/usr/bin/env python3.6

from oblivium.cmd.command import Command


class ClientCmd(Command):
    """Command name"""
    _shell_name = "client"

    def __init__(self, client):
        self.__client = client
        super().__init__()

    def do_start(self, args):
        """Starts the client"""
        self.__client.start()
        print("Client: client was started")

    def do_stop(self, args):
        """Stops the client"""
        self.__client.stop()
        print("Client: client was stopped")
