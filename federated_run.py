# encoding: utf-8

# (c) 2019 - 2023 Open Risk (https://www.openriskmanagement.com)
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

"""
This script illustrates a basic federated estimation workflow
NB: It assumes a certain configuration of model servers is in place
"""

import requests
from ruamel.yaml import YAML

# Load a basic configuration file
yaml = YAML(typ='safe')  # default, if not specified, is 'rt' (round-trip)
config = yaml.load(open('config.yml', 'r'))
hosts = config['hosts']
# Number of epochs to iterate
Epochs = config['epochs']
# Number of participating model servers
n = config['servers']

# Weights to use in the averaging
# TODO remove hardwiring, fetch the node data shape with a controlled API
weights = {'1': 0.25, '2': 0.25, '3': 0.25, '4': 0.25}

# Construct on the fly the list of federating model server URL's
# (The different ports are emulating servers running independently with exchange of data)

url_list = []
for k in range(n):
    model_server_url = hosts + str(k + 1)
    url_list.append(model_server_url)

# Check each model server's status
for k in range(n):
    model_server_url = url_list[k]
    res = requests.get(model_server_url)
    print(res.json())

# Send a start signal to the cluster of model servers and retrieve first parameter estimation
coeffs = {}
intercepts = {}
for k in range(n):
    model_server_url = url_list[k]
    res = requests.get(model_server_url + "/start")
    data = res.json()
    print('Server :', model_server_url, ' Estimates: ', res.json())
    coeffs[str(k)] = data['coefficient']
    intercepts[str(k)] = data['intercept']

# Average the estimated parameters
avg_coef = 0.0
avg_intercept = 0.0
for k in range(1, n):
    avg_coef += weights[str(k)] * coeffs[str(k)]
    avg_intercept += weights[str(k)] * intercepts[str(k)]
data = {'intercept': avg_intercept, 'coefficient': avg_coef}
print('Averaged Estimates: ', data)
print(80 * '=')

# Loop over the desired number of epochs
headers = {'Content-Type': 'application/json'}
for e in range(Epochs):
    # Send averaged parameters to all servers
    # Retrieve new estimates
    print('Epoch: ', e)
    print(80 * '-')
    for k in range(n):
        model_server_url = url_list[k]
        res = requests.post(model_server_url + "/update", json=data, headers=headers)
        data = res.json()
        coeffs[str(n)] = data['coefficient']
        intercepts[str(n)] = data['intercept']
        print('Server :', model_server_url, ' Estimates: ', res.json())

    # Average the updated parameters
    avg_coef = 0.0
    avg_intercept = 0.0
    for k in range(n):
        avg_coef += weights[str(n)] * coeffs[str(n)]
        avg_intercept += weights[str(n)] * intercepts[str(n)]
    data = {'intercept': avg_intercept, 'coefficient': avg_coef}
    print('Averaged Estimates: ', data)

# print final estimate
print('Final Estimate: ', data)
