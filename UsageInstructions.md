# How to use the controller

# Introduction #

Quick start:
  * Force status => all 210 => all ready
  * change ID
  * run, stop

## How to get to the controller ##
First find your Lumikki folder (likely to be in your home folder) and run runuserserver.bash by typing "bash runuserserver.bash" in Terminal. Then open your browser and type "localhost:$lighttpd\_port" onto the address line, where $lighttpd\_port is the port assigned to lighttpd in your user.config file (see [Installation\_user\_conf](Installation_user_conf.md)). In the lab you can find the ports on the door of the humidity chamber.

You can surely use one of the mock servers as well, see [MockDevices](MockDevices.md).

## Overview ##

The user interface consists of a main tab and separate tabs for each device. The main tab is to be used while measuring. Other tabs are used only when defining measurement protocol or while testing. If you have to click on tabs while measuring, you are doing something wrong and you should report an issue.

## Main Tab ##

The main tab consists of three components:
  * control box (top left)
  * status box (top right)
  * log box (bottom)

The control box has three uses:
  * set experiment id
  * start experiment
  * stop experiment

An init button that initializes the devices is on the way. Currently you have to connect to the IR camera on the IR tab and Instron init is done while executing the device side.

## Cam Tab ##

TODO: add content

## TTM Tab (add content) ##

When using TTM, you should first change the parameter "ttm\_global\_port" to 8080 instead of 80, and "ttm\_global\_parentfolder" to C:\data. The default values could probably be fixed quite easily, but for now it's like this.

Meanings of parameters:
ttm\_global\_parentfolder: Data storage path.
ttm\_ramprate: The rate at which the piston moves in cm/s (?) when ttm\_tensile\_channel is set to 1.
ttm\_tensile channel: Here you define whether the parameters concern location (1) or force (2).


## TODO: add following tabs ##