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

from fabric.api import local, parallel
from fabric.context_managers import shell_env
from ruamel.yaml import YAML

yaml = YAML(typ='safe')  # default, if not specfied, is 'rt' (round-trip)
config = yaml.load(open('config.yml', 'r'))
n = config['servers']


def deploy_single():
    with shell_env(FLASK_APP='model_server.py', FLASK_ENV='development'):
        local('flask run --host 127.0.0.1 --port 5000')


def stop_single():
    local('curl localhost:5000/stop')


def deploy_cluster():
    with shell_env(FLASK_APP='model_server.py', FLASK_ENV='development'):
        for i in range(n):
            # local('flask run --host 127.0.0.1 --port 500' + str(i + 1))
            local('/bin/bash ./spawn_server.sh 500' + str(i + 1) + ' &')


def stop_cluster():
    for i in range(n):
        local('curl 127.0.0.1:500' + str(i + 1) + '/stop')
