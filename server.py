#!/usr/bin/env python3.6

from oblivium import Server, ServerCmd

# Echo server program


def main():

    server = Server()

    ServerCmd(server)

    exit(0)


if __name__ == "__main__":
    main()
