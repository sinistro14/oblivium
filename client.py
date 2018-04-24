#!/usr/bin/env python3.6

from oblivium import Client, ClientCmd

# Echo client program


def main():

    client = Client()

    ClientCmd(client)

    print("Client: server was shutdown")

    exit(0)


if __name__ == '__main__':
    main()
