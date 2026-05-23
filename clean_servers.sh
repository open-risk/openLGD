#!/usr/bin/env bash

# stop K flask model_servers using constructed PID's
# ATTN this could kill arbitrary processes

for i in {1..4}
do
    port=$(( 5000 + $i ))
    PID=`lsof -t -i :${port} | sed -n 2p`
    echo ${PID}
    kill -9 ${PID}
done
