#!/usr/bin/env python3.6

import threading
import socketserver

from oblivium.server.server_controller import ServerController


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def start(self):

        # activates server controller
        ServerController(self)

        with self:
            ip, port = self.server_address

            # allows bind to port still in TIME_WAIT state
            self.allow_reuse_address = True

            # Start a thread with the server -- that thread will then start one
            # more thread for each request
            server_thread = threading.Thread(target=self.serve_forever)
            # Exit the server thread when the main thread terminates
            server_thread.daemon = True
            server_thread.start()
            print("Server loop running in thread:", server_thread.name)

            # blocking call
            if input("Press ENTER to shutdown server\n"):
                self.stop()

    def stop(self):
        self.shutdown()
        self.server_close()
