
. lumikki.env


memcached -p 50001 &

lighttpd -f conf/lighttpd.conf -D
