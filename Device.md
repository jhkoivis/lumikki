# Test procedure for TTM #

## Test for tensile protocol ##

  * insert piece of foam to the clamps (folded in that way that there is 6 levels of the foam between the clamps just in case)
  * set ttm\_tensile\_rampamplitude to -50 (put minus if you are using compression clamps)
  * set ttm\_tensile\_ramprate to -0.01 (put minus if you are using compression clamps)
  * start ttm\_logging\_poller, ttm\_start\_poller, ttm\_stop\_poller, ttm\_tensile\_poller, ttm\_variableCalculator\_poller, ttm\_variableSaver\_poller
  * press run
  * check that ttm\_logging\_poller shows linear behavior of displacement (yellow curve)
  * press stop
  * check that movement and logging stopped

## Test for creep protocol ##

  * insert piece of foam to the clamps (folded in that way that there is 6 levels of the foam between the clamps just in case)
  * set ttm\_creep\_load to -10 (put minus if you are using compression clamps)
  * start ttm\_logging\_poller, ttm\_start\_poller, ttm\_stop\_poller, ttm\_creep\_poller, ttm\_variableCalculator\_poller, ttm\_variableSaver\_poller
  * press run
  * check that ttm\_logging\_poller shows constant behavior of force (red curve)
  * press stop
  * check that movement and logging stopped

## Test for tensile-cyclic protocol ##

  * Insert piece of foam to the clamps (folded in that way that there is 6 levels of the foam between the clamps just in case)
  * Set the initial values:
    1. Set ttm\_tensilecyclic\_ramprate to -0.01 (put minus if you are using compression clamps)
    1. Set ttm\_tensilecyclic\_rampsetpoint to -0.04 (put minus if you are using compression clamps)
    1. Set ttm\_tensilecyclic\_ramptargetpressure to -1000 (put minus if you are using compression clamps)
    1. Set ttm\_tensilecyclic\_cyclicamplitude to 0.03
    1. Set ttm\_tensilecyclic\_cyclicfrequency to 0.5
    1. Set ttm\_tensilecyclic\_cyclicsetpoint to -0.06 (put minus if you are using compression clamps)
    1. Set ttm\_tensilecyclic\_sepatarelogging switch down (to take all the data into the same file and making following the test easier)
  * start ttm\_logging\_poller, ttm\_start\_poller, ttm\_stop\_poller, ttm\_tensilecyclic\_poller, ttm\_variableCalculator\_poller, ttm\_variableSaver\_poller
  * Press run
  * Check that the curve goes in right manner:
    1. First, it should go to -0.04 kN to start the ramp part (red force curve).
    1. Then, after waiting, it should do the linear ramp.
    1. Then, again waiting. Then, moving to -0.06 kN to start the cyclic part.
    1. Then, cycles with amplitude of 0.03 kN (not necessary clearly visible due to limited accuracy).
    1. Then repeating as many times as given (default 2 times).
    1. Then, the compression stops, and the displacement curve should be relatively horizontal.
  * Press stop
  * Check that movement and logging stopped

# Test procedure for CAM #

# Test procedure for IR #

## Test for trigger protocol ##

  * Check that FSViewer is running on IR computer
  * press Connect and check connection state from FSViewer
  * set Trigger experiment to 1
  * set Trigger start condition to 2
  * set Trigger start value to 0
  * set Trigger stop condition to 2
  * set Trigger number of images to 1
  * set Trigger source to 0
  * press run
  * send trigger signal to pin 1
  * press stop
  * check that new folder with 1 image has appeared on IR computer under Parent folder

## Test for stream protocol ##

  * Check that FSViewer is running on IR computer
  * press Connect and check connection state from FSViewer
  * set Trigger experiment to 0
  * set Stream start condition to 0
  * set Stream start value to 0
  * set Stream stop condition to 0
  * press run
  * check that image counter in FSViewer is increasing
  * press stop
  * check that new folder with images has appeared on IR computer under Parent folder

# Test procedure for AE #

  * Start DataSocket server on TTM computer. Shortcut is located at Start/All Programs/National instruments/Datasocket/DataSocket server
  * Open ttmServer project on AE computer
  * Start ttm\_aecontrolnew\_poller and ttm\_aecontrol\_AEdata\_read
  * Open aeCap project on AE computer
  * Run Launcher.vi
  * Open Gateway.vi
  * Set setMeasurement, startClock and startCollection to True and write "test" to the filename field. Finally run Gateway.vi.

  * On TTM computer the DataSocket Server window should now show "Processes connected: 2".

  * On TTM computer open ttm\_start.vi
  * Set following values to ttm\_start:
    * ttm\_global\_protocol: aecontrol
    * ttm\_aecontrol\_rampratesilent: 0.01
    * ttm\_aecontrol\_ramprateae: 0
    * ttm\_aecontrol\_timewindow: 1000
    * ttm\_aecontrol\_holdtime: 5000
    * ttm\_aecontrol\_targetvalue: 1
    * ttm\_aecontrol\_aedatasum: 0
    * ttm\_aecontrol\_channel: 1

  * Remove specimen protect from Instron console and run ttm\_start.vi

  * Check that the machine starts pulling at speed of 0.01 mm/s
  * Tap the piezo and make sure that the pull stops for 5 seconds after a single tap.