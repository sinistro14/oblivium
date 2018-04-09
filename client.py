#!/usr/bin/env python3.6

from oblivium.client import Client

# Echo client program


def main():

    client = Client()

    client.start()

    client.stop()

    print("Client: client was shutdown")

    exit(0)


if __name__ == '__main__':
    main()
