#!/bin/bash

. lumikki.env

# load environment similar to conf/cgi.conf

export LUMIKKI_PYTHON_UIDEFAULTS=$lumikki_python_uidefaults
export LUMIKKI_MEMCACHE_IP=$lumikki_memcache_ip
export LUMIKKI_MEMCACHE_PORT=$lumikki_memcache_port

python webroot/cmd/lib/mockserver.py
