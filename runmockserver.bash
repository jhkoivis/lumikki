#!/bin/bash

. lumikki.env

# load environment similar to conf/cgi.conf

echo $lumikki_python_uidefaults

export LUMIKKI_PYTHON_UIDEFAULTS=$lumikki_python_uidefaults
export LUMIKKI_MEMCACHE_IP=$lumikki_memcache_ip
export LUMIKKI_MEMCACHE_PORT=$lumikki_memcache_port

(
echo set cam_ip   0 0 9; echo 127.0.0.1;
echo set ttm_ip   0 0 9; echo 127.0.0.1;
echo set ir_ip    0 0 9; echo 127.0.0.1;
echo set ae_ip		0 0 9; echo 127.0.0.1;
echo set cam_port 0 0 5; echo 40001; 
echo set ttm_port 0 0 5; echo 40002;
echo set ir_port  0 0 5; echo 40003;
echo set ae_port  0 0 5; echo 40004;
sleep 1;
echo quit;
) |telnet $LUMIKKI_MEMCACHE_IP $LUMIKKI_MEMCACHE_PORT


python webroot/cmd/lib/mockserver.py
