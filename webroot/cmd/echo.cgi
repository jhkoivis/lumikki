#!/usr/bin/python

import cgi, cgitb, sys, json
cgitb.enable();

i = sys.stdin.read()
s = json.loads(i)
open('/tmp/lumcgi.log', 'w+').write(i + '\n')

print "Content-Type: application/javascript"
print
print json.dumps(s)

