# oblivium
A Rabin 1-out-of-2 Oblivious Transfer protocol

## Prerequisites
Python version 3.6 is assumed to be installed, as well as pip package manager utility.

## Installation

### Linux
Run "./setup.sh"

### Windows
Run ".\setup.bat"

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

In order to test the protocol, after a client establishes connection to the server, he can
choose a bit (0 or 1) in order to choose a value from the server, which are proposed, randomly,
by the server upon connection.

Run a server and client in two different command windows
Server: > start  
Client: > start  
Client: > b  
Where b is the identifier (0 or 1) of the message to request  
Check that the received message matches the one available at the server  
Shutdown client and server  
Client: > stop  
Client: > exit  
Server: > stop  
Server: > exit  

## Authors
**Group 23**
- **Tiago Gonçalves** - 81853 - (tiago.r.goncalves@tecnico.ulisboa.pt)
- **Ana Neves**       - 90843 - (teresa.goucha@tecnico.ulisboa.pt)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Disclaimer

The presented protocol could be extended to more complex data, however,
as this is only a demo, only integers are used to demonstrated functionality of the service.

Note that this software was develop as an academic project, therefore,
no enterprise level reliability assurances can be provided.
