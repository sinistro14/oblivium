# oblivium
Oblivious Transfer 1-out-of-2 protocol

## Prerequisites
Python version 3.6 is assumed to be installed, as well as pip package manager utility.

## Installation

### Linux
Run ```./setup.sh```

### Windows
Run ```.\setup.bat```

## Setup

### Linux
Start server: ```./run-server.sh```  
Start client: ```./run-client.sh```  

### Windows
Start server: ```.\run-server.bat```  
Start client: ```.\run-client.bat```  

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

In order to test the protocol, after establishing connection to the server, a client is able
to choose a bit (0 or 1) in order to select a value from those available on the server,
which are randomly proposed upon connection.

1. Run a server and a client in two different command windows
```
Server: > start  
Client: > start  
```

2. Request a message, providing the intended message identifier b (0 or 1)
```
Client: > b
```
Notice that the received message matches the one available at the server  

3. Shutdown client and server
```
Client: > stop  
Client: > exit  
Server: > stop  
Server: > exit  
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Disclaimer

The presented protocol could be extended to more complex data, however,
as this is only a demo, only integers are used to demonstrated functionality of the service.

Note that this software was develop as an academic project, therefore,
no enterprise level reliability assurances can be provided.
