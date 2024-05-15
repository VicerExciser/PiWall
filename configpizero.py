import os
import sys

ROUTER='192.168.2.1'
IP_ADDRESS='192.168.2.{0}'
STATIC_IP_BASE=200
HOSTNAME='pi{0}'
# PINAME='tile{0}'
PINAME='pi{0}'

ONLY_NEED_TO_CHANGE_NAMES=False
# NEED_TO_CONNECT_WIFI=False

DHCP_PATH='/etc/dhcpcd.conf'
DHCP='\n\ninterface eth0\nstatic ip_address={0}/24\nstatic routers={1}\nstatic domain_name_servers={1} 8.8.8.8\n'

if __name__=='__main__':
	if len(sys.argv) < 2:
		print('Enter Pi number as arg')
		sys.exit()
	in_num = int(sys.argv[1])
	pinum = STATIC_IP_BASE + in_num
	ip = IP_ADDRESS.format(pinum)
	# name = PINAME.format(pinum)
	name = PINAME.format(in_num)
	host = HOSTNAME.format(pinum)

	# if not ONLY_NEED_TO_CHANGE_NAMES:
	os.system("sudo sed -i 's/gb/us/' /etc/default/keyboard")

	if not ONLY_NEED_TO_CHANGE_NAMES:
		dhcp_cmd = 'sudo echo -e "'+DHCP.format(ip,ROUTER)+'" >> '+DHCP_PATH
		os.system(dhcp_cmd)

	hostname_cmd = 'sudo echo "'+host+'" > /etc/hostname'
	os.system(hostname_cmd)

	if not ONLY_NEED_TO_CHANGE_NAMES:
		host_cmd = 'sudo echo -e "\n{0} {1}" >> /etc/hosts'.format(ip,host)
	else:
		host_cmd = "sudo sed -i 's/{0}/{1}/g' /etc/hosts".format(PINAME.format(pinum),host)
	os.system(host_cmd)

	if not ONLY_NEED_TO_CHANGE_NAMES:
		os.system('sudo adduser '+name)
		os.system('sudo visudo')

	## Add this line to sudoers via visudo:
	#	pi[pinum]	ALL=(ALL:ALL) ALL

	## Remove default user pi:
	# sudo userdel -r pi

	## Then reboot

	