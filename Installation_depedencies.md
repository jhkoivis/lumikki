#Description of programs needed.

# Introduction #

The instructions below explain how to install lumikki to linux like computer. You do not need root priviledges for this.

Most of the packages are also available as precompiled binaries (also for windows). The lumikki itself is written with java and python and thus works with most of the platforms. So if you can find the depedencies, you can use lumikki in your system.

## ubuntu and macport users ##

You can install memcached and memcached python bindings from apt or port. In this case only lighttpd has to be installed manually (see instructions in chapter "Installation of Depedencies" first and second codeblock).

macports:
```
sudo port install memcached py26-memcached
```
note! do not install py-memcached. This is completely different.

ubuntu:
```
sudo apt-get install memcached py26-memcached
```

# Installation of Depedencies #

The following steps need to be executed in the order they are presented. You must choose where to install everything needed to run lumikki. This can be for example a subdirectory 'usr' in your home directory. In this case create it with `mkdir ~/usr` and replace `/prefix/directory` in instructions below with `/<path/<to>/usr`. For example (my usr folder is in /home/jko/usr/):

```
./configure --prefix=/home/jko/usr/
```

Note! You should use **absolute** paths in `/prefix/directory`. You can get the absolute path of the directory (in which you currently are) with command `pwd`.

**lighthttpd
```
mkdir -p ~/src
cd ~/src
wget http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-1.4.28.tar.bz2
tar xjvf lighttpd-1.4.28.tar.bz2
cd lighttpd-1.4.28
./configure --prefix=/prefix/directory
make
make install
```**

Installation is now ready, if you used port or apt to install memcached and its python bindings. If you did not, continue.

**libevent-2.0.10
```
cd ~/src
wget http://monkey.org/~provos/libevent-2.0.10-stable.tar.gz
tar xzvf libevent-2.0.10-stable.tar.gz
cd libevent-2.0.10-stable
./configure --prefix=/prefix/directory
make
make install
```**

**memcached
```
cd ~/src
wget http://memcached.googlecode.com/files/memcached-1.4.5.tar.gz
tar xzvf memcached-1.4.5.tar.gz
cd memcached-1.4.5
./configure --prefix=/prefix/directory
make
make install
```**

**setuptools
```
cd ~/src
wget http://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c11-py2.6.egg#md5=bfa92100bd772d5a213eedd356d64086
mkdir -p /prefix/directory/lib/python2.6/site-packages
export PYTHONPATH=$PYTHONPATH:/prefix/directory/lib/python2.6/site-packages
sh setuptools-0.6c11-py2.6.egg --prefix=/prefix/directory
```**

**memcached-py
```
cd ~/src
wget ftp://ftp.tummy.com/pub/python-memcached/python-memcached-1.48.tar.gz
tar xzvf python-memcached-1.48.tar.gz
cd python-memcached-1.48
export PYTHONPATH=$PYTHONPATH:/prefix/directory/lib/python2.6/site-packages
python setup.py install --prefix=/prefix/directory
```**

Note: 1.48 might not be the latest version of memcached. If python-memcached-1.48.tar.gz is not found on the ftp server, replace "1.48" with "latest" in the filename. If this doesn't work either, google "python memcached" and find the latest version. After you're done, please update these instructions.