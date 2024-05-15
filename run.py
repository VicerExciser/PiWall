import os
import sys
import time
import signal

slave_cmd = 'sshpass -p sh00k parallel-ssh -i -t 40 -h /home/master/backwall -x "-t -t -o StrictHostKeyChecking=no" -A "bash runslave"'

master_cmd = 'avconv -re -i movies/{0} -vcodec copy -f avi -an udp://239.0.1.23:1234'

def playlist_loop():
    while True:
        try:
            for file in os.listdir('/home/master/movies'):
                os.system(master_cmd.format(file))
                time.sleep(0.1)  
        except KeyboardInterrupt:
            sys.exit()

# def play_vid(vid):
#     try:
#         os.system(master_cmd.format(vid))
#         time.sleep(0.1)     
#     except KeyboardInterrupt:
#         sys.exit()  

def receiveSignal(signalNumber, frame):
    # os.system('./stopwall')
    sys.exit()

if __name__=='__main__':
    signal.signal(signal.SIGTERM, receiveSignal)
    os.system(slave_cmd)
    time.sleep(5)
    playlist_loop()
