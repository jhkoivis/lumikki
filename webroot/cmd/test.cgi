#!/usr/bin/python

import cgi, cgitb, sys, json
cgitb.enable(display=0, logdir="/tmp")

f = open('/tmp/jscg.log', 'w+')
f.write(str(sys.stdin.read()) + '\n')

print "Content-Type: application/javascript"
print
print json.dumps({'null':'response'})


