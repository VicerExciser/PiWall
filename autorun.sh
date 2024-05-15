#!/bin/bash

#counter=0
sleep 5s
echo "M A S T E R  B E G I N"
while true; do
  counter=0
  while [ $counter -lt 3 ]; do
    for file in /home/master/movies/*.mp4; do
      avconv -re -i $file -vcodec copy -f avi -an udp://239.0.1.23:1234
    done
    counter=$((counter+1))
  done

  ./stopwall
  #./startwall
  sshpass -p sh00k parallel-ssh -i -t 30 -h backwall -x "-t -t -o StrictHostKeyChecking=no" -A "bash runslave"
  sleep 15s
done
