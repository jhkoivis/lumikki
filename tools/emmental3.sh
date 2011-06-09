
########################################################
# EMMENTAL - your network is full of (secure) holes
########################################################
#
# - create a pipe from controller  to 
#
# hugoputket
username=jko
local_lumikki_ssh=7780
local_ttm_rdesktop=7781

firewall=hugo.hut.fi
lumikki=130.233.202.249
ttm=10.0.0.10

p_rdesktop=3389
p_ssh=22

middlePort1=52759


ssh -ftX $firewall ssh -fN -L $middlePort1:$ttm:$p_rdesktop sauna@$lumikki

ssh -fN -L $local_lumikki_ssh:$lumikki:$p_ssh $username@$firewall # veranta
ssh -fN -L $local_ttm_rdesktop:localhost:$middlePort1 $username@$firewall  # veranta
