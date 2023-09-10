
#  File Server using Multi-threading
A multi-threaded file server that supports Upload, Download, Delete, and Rename file operations

## Requirements
Python 3.0+ with the following libraries installed-

- XMLRPC
- Threading

## Running the Program

1. Open a terminal to run the python files.
2. First, start the server using the following command - \
    $python fileops_server.py 
3. Next, the client code can be executed by opening one or more terminals - \
    $python fileops_client.py
4. The client can use the terminal to perform the desired file operation on the server. (upload, download, rename or delete)


\
**Note**:  The client needs to place the files that are needed to be uploaded in the 'uploads' folder. The downloaded files from the server are placed in the 'downloads' folder.

