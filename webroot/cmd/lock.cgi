#!/usr/bin/env python

from lumilib import *
from config import conf

commandId = 1
try: 
     msg = get_json()
     commandId = msg['id']
     c = conf()
     if 'reset' in msg.keys(): 
          c.mc.set("lock", 0)
          put_json({'id':commandId, "st":0})
     else:
          tryLock = msg["lock"]
          lockValue = c.mc.get("lock")
          if not lockValue or tryLock > lockValue: 
               c.mc.set("lock", tryLock)
          if tryLock <= lockValue:
               raise ValueError("lock fail")
          put_json({'id':commandId, "lock":lockValue, "tryLock":tryLock})
except Exception as e: 
     put_json({'id':commandId, 'st':1, 
               'msg':'Lock failed [' + str(e) + ']'})
    

