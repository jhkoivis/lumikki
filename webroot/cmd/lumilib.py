import json, sys

def log(s): 
    open('/tmp/lumcgi.log', 'a').write(s + '\n')

def put_json(jso):
    s = json.dumps(jso)
    print "Content-type: application/javascript"
    print
    print s
    log('sent: ' + s)

def get_json():
    input = sys.stdin.read()
    log('got: ' + input)
    return json.loads(input)

def get_target(targetId):
    if targetId == 2: 
        return '127.0.0.1'
    else: 
        return None
