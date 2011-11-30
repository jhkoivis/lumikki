
. lumikki.env


memcached -p 38337 &

lighttpd -f conf/lighttpd.conf -D
