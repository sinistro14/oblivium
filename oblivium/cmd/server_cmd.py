#!/usr/bin/env python3.6

from oblivium.cmd.command import Command


class ServerCmd(Command):
    """Command name"""
    _shell_name = "server"

    def __init__(self, server):
        self.__server = server
        super().__init__()

    def do_start(self, args):
        """Starts the server"""
        self.__server.start()
        print("Server: server was started")

    def do_status(self, args):
        """Obtains server status"""
        self.__server.status()

    def do_stop(self, args):
        """Stops the server"""
        self.__server.stop()
        print("Server: server was stopped")
