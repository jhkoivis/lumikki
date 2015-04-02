# How file names should look like

# General #

All output files should have the same format:

```
$DeviceRootFolder/$expID-$timeStamp/$expID-$timeStamp-$theRest
```

  * $DeviceRootFolder: the root folder of the device. This is strongly dependent on the device.
  * $expID: Experiment ID (max 10 characters, IR restriction).
  * $timeStamp: Text produced by the timeStamp.py.
  * $theRest: The device dependent information goes here.

Lumikki sends the $DeviceRootFolder, $expID and $timeStamp. Device parses the path.

## Exceptions ##

  * IR filename does not have $timeStamp.
  * Instron does not have $expID-$timeStamp folder