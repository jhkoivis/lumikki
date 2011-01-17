import json, sys

def log(s): 
    open('/tmp/lumcgi.log', 'a').write(s + '\n')

def putjson(jso):
    s = json.dumps(jso)
    print "Content-type: application/javascript"
    print
    print s
    log('sent: ' + s)

def getjson():
    input = sys.stdin.read()
    log('got: ' + input)
    return json.loads(input)

def gettarget(targetId):
    if targetId == 2: 
        return '127.0.0.1'
    else: 
        return None
