#!/bin/bash
# start 4 xterms
for i in 5001 5002 5003 5004
do
   xterm -hold -e "/bin/bash ./spawn_server.sh $i" &
done