# Installation instructions #

## Installing needed programs and libraries ##

**lumikki**

Get lumikki from the repository by:
```
cd ~
mkdir lumikki
hg clone https://lumikki.googlecode.com/hg/ lumikki
```

The following steps need to be executed in the order they are presented. You must choose where to install everything needed to run lumikki. This can be for example a subdirectory 'src' in your home directory. In this case create it with `mkdir ~/src` and replace `/prefix/directory` in instructions below with `/<path/<to>/src`. For example (my src folder is in /home/jko/src/):

```
./configure --prefix=/home/jko/src/
```

Note! You should use **absolute** paths in `/prefix/directory`. You can get the absolute path of the directory (in which you currently are) with command `pwd`.

**lighthttpd**

```
cd ~/src
wget http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-1.4.28.tar.bz2
tar xjvf lighttpd-1.4.28.tar.bz2
cd lighttpd-1.4.28
./configure --prefix=/prefix/directory
make
make install
```

**libevent-2.0.10**

```
cd ~/src
wget http://monkey.org/~provos/libevent-2.0.10-stable.tar.gz
tar xzvf libevent-2.0.10-stable.tar.gz
cd libevent-2.0.10-stable
./configure --prefix=/prefix/directory
make
make install
```

**memcached**

```
cd ~/src
wget http://memcached.googlecode.com/files/memcached-1.4.5.tar.gz
tar xzvf memcached-1.4.5.tar.gz
cd memcached-1.4.5
./configure --prefix=/prefix/directory
make
make install
```

**setuptools**

```
cd ~/src
wget http://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c11-py2.6.egg#md5=bfa92100bd772d5a213eedd356d64086
mkdir -p /prefix/directory/lib/python2.6/site-packages
export PYTHONPATH=$PYTHONPATH:/prefix/directory/lib/python2.6/site-packages
sh setuptools-0.6c11-py2.6.egg --prefix=/prefix/directory
```

**memcached-py**

```
cd ~/src
wget ftp://ftp.tummy.com/pub/python-memcached/python-memcached-1.47.tar.gz
tar xzvf python-memcached-1.47.tar.gz
cd python-memcached-1.47
python setup.py install --prefix=/prefix/directory
```

## Configuring ##

After everything is installed, lumikki and lightpd need to be configured. You will need to modify several config files (listed below with bold). In the gray boxes below are the modifications you should make. Note that the files already have similar text. Do not enter the text twice, but modify the existing parts.

**~/lumikki/conf/modules.conf**

Make sure that the line including cgi.conf is not commented. It should be like this:
```
##
## plain old CGI (mod_cgi)
##
include "conf.d/cgi.conf"

```

**~/lumikki/conf/conf.d/cgi.conf**

```
#######################################################################
##
##  CGI modules
## --------------- 
##
## http://www.lighttpd.net/documentation/cgi.html
##


alias.url += ( "/cmd" => server_root + "/cmd" )
$HTTP["url"] =~ "^/cmd" {
   setenv.add-environment = ("PYTHONPATH" => "/prefix/directory/lib/python2.6/site-packages")
   cgi.assign = ( ".cgi" => "/usr/bin/python2.6" )


}

##
#######################################################################
```

Modify the path "/prefix/directory/..." to the prefix path the one you are using.

**~/lumikki/lumikki.env**

```
MYPREFIX=/prefix/directory
export PATH=$PATH:$MYPREFIX/sbin:$MYPREFIX/bin
export PYTHONPATH=$PYTHONPATH:$MYPREFIX/lib/python2.6/site-packages
export LD_LIBRARY_PATH=$MYPREFIX/lib
```

Fill correct prefix. Next check that the user has execution rights (symbols 1-3 are rwx):

```
> ls -lha lumikki.env
-rwxr--r-- 1 jko users 189 2011-03-23 14:13 lumikki.env
```

If this is not the case:

```
chmod u+rwx lumikki.env
```

and check again the rights with ls -lha.


**~/lumikki/conf/lighthttpd.conf**

```
#######################################################################
##
## /etc/lighttpd/lighttpd.conf
##
## check /etc/lighttpd/conf.d/*.conf for the configuration of modules.
##
#######################################################################

#######################################################################
##
## Some Variable definition which will make chrooting easier.
##
## if you add a variable here. Add the corresponding variable in the
## chroot example aswell.
##
var.log_root    = "/path/to/lumikki/tmp"
var.server_root = "/path/to/lumikki/webroot"
var.state_dir   = "/path/to/lumikki/tmp"
var.home_dir    = "/path/to/lumikki/tmp"
var.conf_dir    = "/path/to/lumikki/conf"

```

Fill in the correct absolute paths to `lumikki/webroot` and `lumikki/conf` i.e. replace /path/to/lumikki with the installation path of lumikki e.g. /home/jko/lumikki/

Also in multiple user case, server.port must be unique. Look for text below and change server.port to unreserved port. Write down the port number.

```
#######################################################################

##

##  Basic Configuration

## ---------------------

##

server.port=8000
```


**cgi-scripts**

Change the global variables in config.py. Check that comfigurationMap variable has correct g\_logdir and g\_memcacheAddr. The default port number for NEWPORT is 11211.

```
configurationMap = {'g_logdir'        : '~'
    , 'g_memcacheAddr'	: '127.0.0.1:NEWPORT'
    , 'g_active':[False, False, False, False]
    , 'g_measurementid'     : 'default'
    , 'g_timestamp'     : ''
```

If multiple users use lumikki, each of them need to have their own unique port. In this case select a new port and change 'memcached&' in runserver.bash and runuserserver.bash:

```
memcached -p NEWPORT &
```

where NEWPORT is the new port number.


## Running lumikki ##

Start lumikki by running
```
cd ~/lumikki
bash runuserserver.bash
```
You can now use lumikki by opening http://localhost:SERVER.PORT/ in a web browser, where SERVER.PORT is the port you chosed while configuring **lighthttpd.conf** above. The default is http://localhost:8000/

## Troubleshooting ##

**2011-03-19 15:07:47: (plugin.c.169) dlopen() failed for: /prefix/directory/lib/mod\_indexfile.so**

**/prefix/directory/lib/mod\_indexfile.so: cannot open shared object file: No such file or directory**

**2011-03-19 15:07:47: (server.c.650) loading plugins finally failed**

The plugin library is wrong. Tell lighttpd where mod\_indexfile.so is. A quick fix is to add "-m /path/to/lib" after "lighttpd -f conf/lighttpd.conf -D" in runuserserver.bash. Runuserserver.bash should look like (my prefix directory is /home/jko/usr/):

```
. lumikki.env
memcached&
lighttpd -f conf/lighttpd.conf -D -m /home/jko/usr/lib
```

Longer fix is to reinstall lighttpd with correct prefix. Remove the lighttpd-1.4.28.tar.bz2 and lighttpd-1.4.28 directory and download the stuff again. Then do bullet **lighthttpd** above again. Removing the stuff makes sure that there is no old configurations left behind.

**failed to listen on TCP port 11211: Address already in use**

Your memcached default port is reserved. Someone else is using it. Most likely other memcached. Kill it with 'killall memcached'. If this does not work, you either have to free the port or use alternative port. To use alternative port you have to replace 11211 with the new port number (between 10000 - 50000) in the following line in 'webroot/cmd/config.py':

```
self.mc = memcache.Client(['127.0.0.1:11211'], debug=0)
```

and change 'memcached&' in runserver.bash and runuserserver.bash:

```
memcached -p NEWPORT &
```
where NEWPORT is the new port number.

Used ports can be seen with 'netstat -tap' (third column, after :).

**memcached**

You can test memcached with the following commands (text after > is what you type). Before and after running the test, kill existing memcached with 'killall memcached'.

```
> memcached &
> telnet localhost 11211
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
> get greeting
END
> set greeting 1 0 11
> Hello World
STORED
> get greeting           
VALUE greeting 1 11
Hello World
END
> quit
```
