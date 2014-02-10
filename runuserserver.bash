
. lumikki.env

echo memcached -p $lumikki_memcache_port 
memcached -p $lumikki_memcache_port &

echo lighttpd -f $lumikki_config_path/lighttpd.conf -D
lighttpd -f $lumikki_config_path/lighttpd.conf -D
