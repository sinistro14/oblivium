#!/usr/bin/env python3.6

import socket

# Encoding type
DEFAULT_ENCODING = 'utf-8'

# TCP socket_utils info
SOCKET_TYPE = socket.SOCK_STREAM    # TCP
SOCKET_AF = socket.AF_INET          # address family

# Server info
SERVER_HOST = 'localhost'
SERVER_PORT = 10000                 # expected to be a free port

# Data info
BYTES_TO_READ = 2048                # maximum bytes to be read from socket
SERVER_HANDLER_TIMEOUT = 20         # server listener handlers timeout
CLIENT_HANDLER_TIMEOUT = 20         # client handler timeout
