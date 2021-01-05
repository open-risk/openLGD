#!/bin/bash
# starts 4 docker containers providing NPL data
# stop them with docker stop $(docker ps -a -q)
for i in 8001 8002 8003 8004
do
   docker run -p $i:8080 openrisk/opennpl_web:0.1.2 &
done