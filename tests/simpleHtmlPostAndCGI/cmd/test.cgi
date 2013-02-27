#!/usr/bin/python
import sys, json

instr = sys.stdin.read()

a = open('/tmp/test.log','a')
a.write('%s\n' % (instr))
a.close()

b = {}
b["hello"] = "from test.cgi"



print "Content-type: application/javascript"
print ""
print json.dumps(b)
