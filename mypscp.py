import os
import sys
import subprocess
import pexpect

infile = sys.argv[1]

with open('backwall') as wall:
	for line in wall:
		line = line.rstrip()
		user, host = line.split('@')
		print('User:['+user+'] - Host:['+host+']')
		dest = '/home/'+user+'/'
		cmd = "scp "+infile+" "+line+":"+dest
		print(cmd)
		# os.system(cmd)
		subprocess.run(cmd, input=b'sh00k', shell=True)
		
		# child = pexpect.spawn(cmd)
		# child.expect(line+"'s password: ")
		# child.sendline('sh00k')

"""
subprocess.run(args, *, 
				stdin=None, 
				input=None, 
				stdout=None, 
				stderr=None, 
				capture_output=False, 
				shell=False, 
				cwd=None, 
				timeout=None, 
				check=False, 
				encoding=None, 
				errors=None, 
				text=None, 
				env=None, 
				universal_newlines=None)
"""