#!/usr/bin/env bash
# start a flask model_server at port number given as first command line argument
export FLASK_APP=model_server.py
export FLASK_ENV=development
export PYTHONPATH=$PYTHONPATH:./
flask run --host 127.0.0.1 --port $1
