import os
import sys
import signal

cmd = 'avconv -re -i movies/{0} -vcodec copy -f avi -an udp://239.0.1.23:1234'

def playlist_loop():
    while True:
        try:
            for file in os.listdir('/home/master/movies'):
                os.system(cmd.format(file))
        except KeyboardInterrupt:
            sys.exit()

def receiveSignal(signalNumber, frame):
    # os.system('./stopwall')
    sys.exit()

if __name__=='__main__':
    signal.signal(signal.SIGTERM, receiveSignal)
    playlist_loop()
