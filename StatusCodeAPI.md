# Introduction #

The status codes of lumikki and it's devices should be implemented throughout the code as defined here. Errors should be raised towards the user, but to a status queries there should be a response defined by one of these codes.

All devices should return at least three status codes:

210: ready

220: measuring

240: not ready

# Details #

The main definition of status codes is given in errmap in lumikki.js.

Implementation of new statuses should be done there and their description should be written in here.

The codes are categorized as follows:

0-hundred codes are for lumikki's internal statuses

1-hundred codes are for connection statuses between lumikki and it's devices

2-hundred codes are for devices internal statuses

Ex.

To a status query a device should always respond with a two hundred code.

# Mapping #

"000":"Cannot connect to anything"

"010":"Server sent unknown status"

"020":"Server response did not contain status"

"100":"Disabled from server."

"110":"Target machine did not respond"

"120":"Server received malformed command."

"122":"Connection refused."

"130":"Not implemented."

"200":"Target available, values not set"

"210":"Ready to measure"

"220":"Measuring"

"230":"System is busy, please try again in a while."

"240":"Measurement device error"