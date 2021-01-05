#!/bin/bash
# starts 4 xterms for monitoring the servers
for i in 5001 5002 5003 5004
do
   xterm -hold -e "/bin/bash ./spawn_server.sh $i" &
done