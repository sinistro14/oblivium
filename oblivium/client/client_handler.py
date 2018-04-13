#!/usr/bin/env python3.6

from oblivium.common.messages import InitialMessage


class ClientHandler:

    """
    The request handler class for our client

    Must override the handle method to implement communication with the
    server
    """

    def __init__(self, client):
        self.__client = client

    def send(self, data):
        self.__client.send(data)

    def receive(self):
        return self.__client.receive()

    def handle(self):
        print("Input message or type 'q' exit")
        while True:
            message = input("Message to send -> ")
            if message and message != "q":  # input "q" to exit
                self.send(InitialMessage(message))
                response = self.receive()  # ResponseMessage
                print("Received from server -> " + str(response.get_string()))
            else:
                break
