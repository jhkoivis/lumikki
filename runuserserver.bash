
. lumikki.env

memcached -p $lumikki_memcache_port &

lighttpd -f $lumikki_config_path/lighttpd.conf -D
