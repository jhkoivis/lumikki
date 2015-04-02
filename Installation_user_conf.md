#Installation instructions for branch named user\_conf

# Introduction #

This page describes how to install and use "new" branch of lumikki called user\_conf. This branch differs from the original s.t. all user dependent information is stored in one file.

The reason is that the installation is easier, read: does not require so much knowledge of the technical details of javascript, lighttpd, memcached, etc.

The drawback is that you lose some features e.g. you cannot use variables in config file => lots of copy-paste (Reason for this is that the file is read by lighttpd, bash and python).

# Installation #

First of all, get lumikki from the repository by:
```
cd ~
mkdir lumikki
hg clone https://lumikki.googlecode.com/hg/ lumikki
```

After this, install all depedencies described in [Installation\_depedencies](Installation_depedencies.md).

Then in your lumikki folder, update to user\_conf branch by typing:
```
hg update user_conf 
```


# Configuration #

There is only one file that you should edit: **conf/user.conf**. By default, this file does not exist in repository and it should not exists (multiple users -> commit -> overwritten -> rewrite it in every update).

In the following, **$install\_path** is the installation path of lumikki e.g. /home/jko/lumikki.

Create user.conf by copying the template:
```
cd $install_path
cp conf/user.conf.orig conf/user.conf
```

Edit the file with your favourite editor, e.g.
```
gedit $install_path/conf/user.conf
```

Change the variables as follows where $X\_Y is something that you replace, see below:
```
# general variables
lumikki_prefix="$depedency_prefix"
lumikki_config_path="$install_path/conf"

# memcache configurations
lumikki_memcache_ip="127.0.0.1"
lumikki_memcache_port="$memcache_port" 

# cgi python environment
lumikki_python_pythonpath="$depedency_prefix/lib/python2.6/site-packages"
lumikki_python_cgiassign="$python_binary"
lumikki_python_uidefaults="$install_path/webroot/html/variables.xml"

# lighttpd conf
lumikki_lighttpd_port="$lighttpd_port"
lumikki_lighttpd_log_root="$install_path/tmp"
lumikki_lighttpd_state_dir="$install_path/tmp"
lumikki_lighttpd_server_root="$install_path/webroot"
lumikki_lighttpd_home_dir="$install_path"
```

$depedency\_prefix = where you installed depedencies e.g. /home/jko/usr or /usr (this contains bin and lib folders). see [Installation\_depedencies](Installation_depedencies.md) and caveats below.

$memcache\_port = free port for memcache (number from 10000 - 50000)

$python\_binary = path to python binary e.g. /usr/bin/python2.6

$lighttpd\_port = free port for lighttpd (number from 10000 - 50000)


# caveats #

lumikki\_python\_pythonpath has to containg all the python packages that are used by lumikki\_python\_cgiassign. Notice, that you may have to change it if you have site-packages in a different folder...