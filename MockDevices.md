# Introduction #

For each device, a mock is created. This enables testing of lumikki functionality without the use of measurement apparatus.

# Quick Start #

In terminal 1:
```
./runmockserver
```
In terminal 2:
```
./runuserserver
```
Change ip and port in lumikki ui (in firefox, goto http://localhost:$MYPORT). for example, ip and port for ttm are 127.0.0.1 and 40002. Starting experiment changes the ttm status (seen when pressed "force status").

# Details #

runmockserver.bash runs four mock servers on localhost, ports 40001-40004.

The devices are configured in:
lumikki/webroot/cmd/lib/mockdevices.py

Currently functionality of ttm and ir are supported.