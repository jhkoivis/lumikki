#!/bin/sh

server=$1
tmpFn=./tmpFile_remove.`date +%s`

echo echo
echo echo If the following fails, do the following:
echo echo
echo echo cd ~/.ssh
echo echo ssh-keygen -t rsa
echo echo "hit enters \(plank passwords\)"
echo echo exec ssh-agent
echo echo

echo scp $server:~/.ssh/authorized_keys $tmpFn
echo cat ~/.ssh/id_rsa.pub \>\> $tmpFn
echo scp $tmpFn $server:~/.ssh/authorized_keys
echo rm $tmpFn
#echo ssh $server cat .ssh/id_rsa.pub \>\> ~/.ssh/authorized_keys
#echo ssh exec ssh-agent



