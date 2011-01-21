#########################################################################
# 
# Custom LabVIEW TCP Server Client Script
# 
# Copyright (C) 2002,2003 Jim Kring jim@jimkring.com
#
# Visit OpenG.org for the more info on Open Source LabVIEW Projects
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
# 
#########################################################################


# Little modifications: Jani Saarenpaa. TKK summer 2009.

import socket as _socket

# sauna:
# _serverHost = '130.233.205.151'

# kamera:
#_serverHost = '130.233.203.154'

#_serverPort = 6423
# _serverPort = 7561
isConnected = 0
_sockobj = None


def connect(_serverHost, _serverPort):
    'opens a connection to LabVIEW Server'
    global _sockobj, isConnected
    _sockobj = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    try:
        _sockobj.settimeout(5)
        _sockobj.connect((_serverHost, _serverPort))   # connect to LV
        isConnected = 1
        return 0
    except _socket.error:
        raise ValueError(
"""Error connecting to camera server. Check if you have the right 
ip and port. Also check if Labview is running and waiting for the message.""")
        


def disconnect():
    'closes the connection to LabVIEW Server'
    global isConnected
    _sockobj.close()                             # close socket
    isConnected = 0


def _passCommand(command):
    'passes a command to LabVIEW Server'
    _sockobj.send(command)
    data = _sockobj.recv(65536)
    #execString = "lvdata = " + data
    #exec execString
    #return lvdata
    return data


class _Instrument:
    
    def __init__(self, _instrumentName, _functionNames):
        
        for _functionName in _functionNames:
            _execString = "self." + _functionName + " =_Function('" + _instrumentName + "." + _functionName + "')"
            exec _execString


class _Function:
    
    def __init__(self, name):

        self._name = name

    def __call__(self, a = None):

        if isConnected:        
        
            if (a == None):
            
                return _passCommand(self._name + '()')
        
            else:
            
                return _passCommand(self._name + '(' + `a` + ')')

        else: raise ValueError('Not Connected: Run "%s.connect()" method to connect.'% __name__)


#connect()

#_instrumentList = _passCommand("System.Get_Instruments()")

#for _instrument in _instrumentList:
#    _instrumentName = _instrument[0]
#    _instrumentFunctionList = _instrument[1]
#    _execString = _instrumentName + ' = _Instrument(' + `_instrumentName` + ",  " + `_instrumentFunctionList` +')'
#    exec _execString

#disconnect()
