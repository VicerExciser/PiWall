import os
import sys
import subprocess
import shlex

if len(sys.argv) > 1:
	incmd = ' '.join(sys.argv[1:])
else:
	incmd = "python3 videoloop.py"

cmdframe = '"{}"'.format(incmd)
cmd = 'sshpass -p sh00k parallel-ssh -i -t 0 -h backwall -x "-t -t -o StrictHostKeyChecking=no" -A "{}"'.format(cmdframe)
#os.system(cmd)
subprocess.call(cmd, shell=True)
#subprocess.Popen(shlex.split(cmd), shell=True)

# with open('backwall') as wall:
# 	for line in wall:
# 		line = line.rstrip()
# 		user, host = line.split('@')
# 		# print('User:['+user+'] - Host:['+host+']')
# 		dest = '/home/'+user+'/'
# 		cmd = 'ssh {0} -t -t -o StrictHostKeyChecking=no {1} &'.format(line,cmdframe)
# 		# cmd = "sshpass -p sh00k ssh {0} -t -t -o StrictHostKeyChecking=no {1} &".format(line,cmdframe)
# 		print(cmd)
# 		os.system(cmd)
# 		# subprocess.run(cmd, input=b'sh00k', shell=True)
		
# 		# child = pexpect.spawn(incmd)
# 		# child.expect(line+"'s password: ")
# 		# child.expect("password:")
# 		# child.sendline('sh00k')
# 		# child.expect('[sudo] password for '+user+': ')
# 		# child.sendline('sh00k')

