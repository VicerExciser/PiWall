# [[[  PiWall  ]]]

1. Master pi is router and DHCP server, informs all slaves of their address
2. Master acts a bridge and the slaves learn their addresses from router


Slave pis on 192.168.2.X subnetwork

Master will have wlan0 address 192.168.1.X, and eth0 address 192.168.2.1 — broadcasting on 192.168.2.255, gateway being 192.168.1.1 router
 
=============================

[  OS Flavor:  Raspbian Stretch Lite  ]

=============================

Master
	•	hostname: piwall
	•	static IP: 192.168.54.254

## backwall:
	pi1@192.168.2.201
	pi2@192.168.2.202
	pi3@192.168.2.203
	pi4@192.168.2.204
	pi5@192.168.2.205
	pi6@192.168.2.206
	pi7@192.168.2.207
	pi8@192.168.2.208
	pi9@192.168.2.209
	pi10@192.168.2.210
	pi11@192.168.2.211
	pi12@192.168.2.212

=============================

Slaves (Board #N)
	•	hostname: pi{N}    (e.g., pi207)
	•	static IP [eth0]: 192.168.2.{N}/24  (in /etc/dhcpcd.conf)
	•	username: pi{200 - N}   (e.g., pi7)
	•	password: sh00k

#  TO REBUILD:

1.) Enable SSH & SCP over the script ‘configpizero.py’

2.) `sudo python3 configpizero.py {200 - N}`   # (pass it the Pi number as arg)

3.) Add this line to sudoers via visudo:  
	pi{N}	ALL=(ALL:ALL) ALL
	
4.) Reboot & login as ‘pi{200 - N}’ w/ password ‘sh00k’
>> or, `sudo login pi9`

5.) SCP over these scripts:
	- install.sh
	- makepiwall.py
	- runslave
	- hdmi_to_component.sh

6.) `./install.sh`

7.) `python3 makepiwall.py {200 - N}`   # (pass it the Pi number as arg)


#  CONFIGS:

## Set /etc/hostname:
	pi{N}     # (e.g., pi201, pi212)

## Append to /etc/hosts:
	192.168.2.{N}  pi{N}    # (e.g., 192.168.2.209  pi209)

## Append to /etc/dhcpcd.conf:
	interface eth0
	static ip_address=192.168.2.{N}/24
	static routers=192.168.2.1
	static domain_name_servers=8.8.8.8

## Last line of ~/.bashrc:  
	./runslave

## runslave:
	#!/bin/bash
	ADDR="239.0.1.23"
	PORT=1234
	BUFSIZE=200000  #400000
	URL="udp://${ADDR}:${PORT}?buffer_size=${BUFSIZE}B”
	echo "[ $(hostname) ]  Listening on UDP"
	pwomxplayer -A $URL


## For disabling HDMI output in favor of component:
### in /boot/config.txt:
-	Comment out ‘hdmi_force_hotplug=1’
-	Set ‘sdtv_mode=2’	(_ I think… might be 0 _)


____________________________________________


# Fix for PiWall stopping:
> sudo nano /usr/local/bin/restart
>>	#!/bin/bash
	sshpass -p sh00k sudo bash $HOME/rebootall

In autorun.sh:
	Rather than evoking all slaves after ‘./stopwall’
	>> restart

____________________________________________


# Refs
http://www.piwall.co.uk/information/installation
http://www.piwall.co.uk/information/configuration-file  
http://matthewepler.github.io/2016/01/05/piwall.html
https://sharmamohit.com/work/project/vizwall/ ********
http://portal.desktopgridfederation.org/web/dutch-chapter/video-wall
https://www.rossmonroe.com/red-bull-pi-wall

