########################################################
# EMMENTAL - your network is full of (secure) holes
########################################################
#
# passwordless login: 
# http://blogs.translucentcode.org/mick/archives/000230.html
#
# memcached: 38333 + X
# lumikki-UI: 39333 + X
#

username=$1
id=0

case "$username" in
	jko)
	id=1
	;;
	amandine)
	id=2;
	;;	
	ovaskav1)
	id=3;
	;;	
	mmyntti)
	id=4;
	;;	
	aphonkan)
	id=5;
	;;	
	epursiai)
	id=6;
	;;
        makinet3)
	id=12;
	;;
	*)
	echo
	echo EMMENTAL - your network is full of \(secure\) holes
	echo
	echo usage:
	echo
	echo $0 username
	echo $0 username \| bash	
	exit;
	;;
esac

local_ttm_rdesktop=$[31770 + $id]
local_cam_rdesktop=$[32770 + $id]
local_ir_rdesktop=$[33770 + $id]
local_ae_rdesktop=$[34770 + $id]

firewall=hugo.hut.fi
erin=erin.hut.fi
ttm=10.0.0.10
cam=10.0.0.20
ir=10.0.0.30
ae=10.0.0.40

p_rdesktop=3389

middlePort_ttm=$[41333 + $id]
middlePort_cam=$[42333 + $id]
middlePort_ir=$[43333 + $id]
middlePort_ae=$[44333 + $id]

echo
echo echo ttm:
echo ssh -ftX $firewall ssh -fN -L $middlePort_ttm:$ttm:$p_rdesktop 	$username@$erin
echo ssh -fN -L $local_ttm_rdesktop:localhost:$middlePort_ttm $username@$firewall 
echo
echo echo cam:
echo ssh -ftX $firewall ssh -fN -L $middlePort_cam:$cam:$p_rdesktop 	$username@$erin
echo ssh -fN -L $local_cam_rdesktop:localhost:$middlePort_cam $username@$firewall 
echo
echo echo ir:
echo ssh -ftX $firewall ssh -fN -L $middlePort_ir:$ir:$p_rdesktop 	$username@$erin
echo ssh -fN -L $local_ir_rdesktop:localhost:$middlePort_ir $username@$firewall 
echo
echo echo ae:
echo ssh -ftX $firewall ssh -fN -L $middlePort_ae:$ae:$p_rdesktop 	$username@$erin
echo ssh -fN -L $local_ae_rdesktop:localhost:$middlePort_ae $username@$firewall
echo

# echo instructions
echo echo ttm: rdesktop localhost:$local_ttm_rdesktop -k fi -f -rdisk:home=/home/$username/ -rdisk:tmp=/tmp/ 
echo echo cam: rdesktop localhost:$local_cam_rdesktop -k fi -f -rdisk:home=/home/$username/ -rdisk:tmp=/tmp/
echo echo ir: rdesktop localhost:$local_ir_rdesktop -k fi -f -rdisk:home=/home/$username/ -rdisk:tmp=/tmp/
echo echo ae: rdesktop localhost:$local_ae_rdesktop -k fi -f -rdisk:home=/home/$username/ -rdisk:tmp=/tmp/











