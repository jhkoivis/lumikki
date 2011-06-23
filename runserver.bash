memcached&
MPID=$!
lighttpd -f conf/lighttpd.conf -D
kill $MPID