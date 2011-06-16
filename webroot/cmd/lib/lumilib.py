import json, sys, os, config

def log(s):
    c = config.conf()
    path = os.path.expanduser(c.get('g_logdir')) + '/lumcgi.log'
    open(path, 'a').write(s + '\n')
    #except IOError:
    #    open(c.get('g_logdir') + '/lumcgi')

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
