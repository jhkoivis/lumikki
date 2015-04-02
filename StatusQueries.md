#Defines minimum status queries every machine should fulfill.

**DEPRECATED use statusCodeApi wiki page instead of this one.**

# Status Queries #

All devices response to status queries. Responce is a json string:

```
{'status':'X', 'statusText':'Y'}
```

Y is free human readable description what is happening. X is picked from the following list:

```
200 ready
220 measuring
240 not-ready (service unavailable)
```

  * 200 is returned only if 'start' command can be the next command.

  * 220 is returned only if data is being written to disk (logging is on, pictures are taken, trigger is armed and trigger signal should arrive). Note that for instance, moving crosshead without logging is not 220.

  * In all the other cases 503 is returned.