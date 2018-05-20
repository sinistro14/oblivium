# oblivium

## Installation
Python version 3.6 is required and assumed to be installed, as well as pip installer utility.

### Linux
Run "./setup.sh"

### Windows
run ".\setup.bat"

## Setup

### Linux
Start server: "./run-server.sh"
Start client: "./run-client.sh"

### Windows
Start server: ".\run-server.bat"
Start client: ".\run-client.bat"

## How to run

### Linux and Windows

For both server and client instances the following commands are available:

help - lists the available commands
exit - exits the application

#### Server

start - launch server request handler
stop - stops server request handler
status - informs whether the server is waiting for new client requests

#### Client

start - establishes communication with the server
stop - stops communication with the server, stop client handler

## Example run

Run a server and client in two different command windows
Server: > start
Client: > start
Client: > <b> , where b is the message to request
Check that the received message matches the one available at the server
Shutdown client and server
Client: > stop
Client: > exit
Server: > stop
Server: > exit

## Disclaimer
Note that this software was develop as an academic project, therefore,
no enterprise level reliability assurances can be provided.