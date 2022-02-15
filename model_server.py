# encoding: utf-8

# (c) 2019 - 2022 Open Risk (https://www.openriskmanagement.com)
#
# openLGD is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of openLGD. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

""" This module provides a model server that has local access to distributed data sources

Each federated model server makes three endpoints available
1) GET localhost:/          API Root, indicating the server is live
2) GET localhost:/start     URL to get initial locally estimated parameters (cold start)
3) POST localhost:/update   URL to post current averaged parameters (warm start)
"""

import json
import os
import signal
from urllib.parse import urlparse

from flask import Flask, jsonify, request

from lgdModel import lgdModel

app = Flask(__name__)


def start_calculation():
    url = urlparse(request.host)
    port = url.path.split(':')[-1]
    n = int(port) - 5000
    initial_params = lgdModel(server=n)
    return initial_params


def update_calculation(params):
    url = urlparse(request.host)
    port = url.path.split(':')[-1]
    n = int(port) - 5000
    intercept = params['intercept']
    coef = params['coefficient']
    updated_params = lgdModel(server=n, intercept=intercept, coef=coef)
    return updated_params


@app.route('/start', methods=['GET'])
def start():
    initial_params = start_calculation()
    return initial_params


@app.route('/update', methods=['POST'])
def update():
    print('Headers', request.headers)
    old_params = json.loads(request.data.decode('utf-8'))
    new_params = update_calculation(old_params)
    return new_params


@app.route('/stop', methods=['GET'])
def stop():
    sig = getattr(signal, "SIGKILL", signal.SIGTERM)
    # os.kill(os.getpid(), sig)
    # os.kill(os.getpid(), signal.SIGINT)
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return jsonify({"success": True, "message": "Server is shutting down..."})


@app.route('/')
def hello_world():
    resp = {'message': 'Hello Federated Credit Risk Models!', 'from server': request.host}
    return resp


if __name__ == '__main__':
    app.run(debug=True)
