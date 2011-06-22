
. lumikki.env


memcached -p 38336 &

lighttpd -f conf/lighttpd.conf -D
