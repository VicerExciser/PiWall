import os
import sys

if len(sys.argv) < 2:
	print('Missing arg (slave[n]): n | [1 2 ...] | all')
	sys.exit()
slaves = ' '.join(sys.argv[1:])
cmd = 'sshpass -p sh00k ssh {0}'
if slaves == 'all':
	with open('backwall') as wall:
		for line in wall:
			os.system(cmd.format(line.rstrip()))
else:
	for n in slaves.split():
		pinum = 200 + int(n)
		pi = 'pi'+n
		host = '192.168.2.'+str(pinum)
		target = '{}@{}'.format(pi,host)
		os.system(cmd.format(target))
