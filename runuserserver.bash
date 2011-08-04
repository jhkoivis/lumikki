
. lumikki.env


memcached -p 38339 &

lighttpd -f conf/lighttpd.conf -D
