
. lumikki.env


memcached -p 38338 &

lighttpd -f conf/lighttpd.conf -D
