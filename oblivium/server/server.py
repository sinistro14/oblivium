#!/usr/bin/env python3.6

import threading
import socketserver

from oblivium.common import network_constants
from oblivium.server.server_handler import ServerHandler


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Server handler launcher thread"""
    __server_thread = None

    def __init__(self):
        super().__init__(
            (network_constants.SERVER_HOST, network_constants.SERVER_PORT),
            ServerHandler
        )

    def start(self):
        """Starts server"""

        # allows bind to port still in TIME_WAIT state
        self.allow_reuse_address = True

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        self.__server_thread = threading.Thread(target=self.serve_forever)
        # Exit the server thread when the main thread terminates
        self.__server_thread.daemon = True
        self.__server_thread.start()
        print("Server loop running in thread: ", self.__server_thread.name)

    def status(self):
        """Returns server status"""
        if self.__server_thread and self.__server_thread.is_alive():
            print("Server is running")
        else:
            print("Server is stopped")

    def stop(self):
        """Stops server"""
        self.shutdown()
        self.server_close()
