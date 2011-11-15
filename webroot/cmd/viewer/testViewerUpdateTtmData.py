
import json
import urllib2
import random

testData = [] 
for i in range(10):
    testData.append(random.random())

params = json.dumps({"analogStrain"    : testData,
                     "stress"          : testData,
                     "digitalStrain"   : testData})

headers = {"Content-type" : "application/javascript"}

#s = "Content-type : application/javascript\n\n"
s = params + '\n'
#s = '{"s": "a"}'

#print s
req = urllib2.Request(url = "http://127.0.0.1:39334/cmd/viewer/viewerUpdateTtmData.cgi",
                      data = s)
f = urllib2.urlopen(req)
#print f.read()

