#!/bin/bash
HOST="dl.piwall.co.uk"
DEB1="pwlibs1_1.1_armhf.deb"
DEB2="pwomxplayer_20130815_armhf.deb"

sudo userdel -r pi 
# sudo apt-get update 
sudo apt-get upgrade -y
sudo apt-get install -y wget omxplayer libegl1-mesa-dev libav-tools sshpass toilet parallel-ssh

wget ${HOST}/${DEB1}
sudo dpkg -i "${HOME}/${DEB1}"
rm "${HOME}/${DEB1}"

wget ${HOST}/${DEB2}
sudo dpkg -i "${HOME}/${DEB2}"
rm "${HOME}/${DEB2}"

echo -e "\nif [ -f 'runslave' ] ; then ./runslave ; fi\n" >> ~/.bashrc

if [ -f 'hdmi_to_component.sh' ]; then 
	./hdmi_to_component.sh 
fi

sudo usermod -a -G video $(whoami)
sudo reboot