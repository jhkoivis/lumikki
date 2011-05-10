
"""
    This is a simple test case for lumikki clients.
    You create a sockobject and write stuff to it.
    
    usage:
            python run_simpleJSON.py
    
    JSON formulation is done by lumilib.put_json() 
    in createMessage. 
    
    
"""

import sys
sys.path.append('../webroot/cmd/')
import lumilib
import StringIO
import socket as _socket


def connect(_serverHost, _serverPort):
    'opens a connection to server'
    global _sockobj, isConnected
    _sockobj = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    try:
        _sockobj.settimeout(5)
        _sockobj.connect((_serverHost, _serverPort))  
        isConnected = 1
        return 0
    except _socket.error:
        raise 
        
def passCommand(command):
    'passes a command to server'
    _sockobj.send(command)
    data = _sockobj.recv(65536)

    return data

def disconnect():
    'closes the connection to server'
    global isConnected
    _sockobj.close()                             # close socket
    isConnected = 0

def createMessage():
    """
        Creates the message to be sent to server.
    """
    # redirect data stream
    dataFile = StringIO.StringIO()
    sys.stdout = dataFile
    
    # create JSON data
    lumilib.put_json({'test':123})
    
    # redirect stream back to stdout
    sys.stdout = sys.__stdout__
    
    # get data as string
    dataFile.seek(0)
    dataString = ""
    for line in dataFile:
        dataString += line
    
    return dataString



if __name__ == '__main__':
    
    message = createMessage()
    # connect and send data
    connect('127.0.0.1', 12378)
    passCommand(message)
    disconnect()
