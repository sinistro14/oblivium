#!/usr/bin/env python3.6


class ClientHandler:

    def __init__(self, client):
        self.__client = client

    def send(self, data):
        self.__client.send(data)

    def receive(self):
        return self.__client.receive()

    def handle(self):
        while True:
            message = input("Message to send -> ")
            if message and message != "q":  # input "q" to exit
                self.send(message)
                response = str(self.receive())
                print("Received from server: " + response)
            else:
                break
