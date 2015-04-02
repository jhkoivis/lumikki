# Installation instructions for infrared camera

# INSTALLATION INSTRUCTIONS #

## Quick start ##

  * start Ligthttpd server (passes http-post to MessageSenderCon)
  * start FSViewer.exe (located in ircamera/FSviewer/Debug/)
  * test setup with MessageSenderCon (located in `<`LighttpdDir`>`/htdocs)

### Starting Lighttpd server ###
```
LightTPD.exe -f conf/lighttpd-inc.conf -m lib -D
```
### Starting FSViewer.exe ###
```
FSViewer.exe
```
click connect button.

### Testing with messageSenderCon ###

`<`enter`>` means press enter, <ctrl+z> means press press ctrl and z down (EOF in windows, ctrl+d in `*`nix)

```
MessageSenderCon.exe
{"focus":0}<enter>
<ctrl+z><enter>
```

### Sample Instructions ###
```
{
"expId":"test",
"filename":"test.img",
"path":"D:\",
"framerate":"30",
"recordTime":"1",
"storeCondition":"1",
"stopCondition":"1",
"startCondition":"1",
"startValue":"1",
"storeValue":"1",
"recordFormat":"1",
"trigSource":"1",
"autoShutter":"1"
}
```
## Contents (of ircamera folder) ##

- Programming samples include simple programs
- LightTPD folder includes working LightTPD server.

Configuration works if LightTPD folder is copied
to root folder (C:\). Command to start the server
is:

LightTPD.exe -f conf/lighttpd-inc.conf -m lib -D

in C:\LightTPD folder.