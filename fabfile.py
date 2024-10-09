# encoding: utf-8

# (c) 2019 - 2024 Open Risk (https://www.openriskmanagement.com)
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

from fabric import task
from ruamel.yaml import YAML

yaml = YAML(typ='safe')  # default, if not specified, is 'rt' (round-trip)
config = yaml.load(open('config.yml', 'r'))
n = config['servers']


@task
def hello(ctx):
    print("Hello Federated Risk Models")


@task
def deploysingle(ctx):
    ctx.config.run.env = {'FLASK_APP': 'model_server.py', 'FLASK_ENV': 'development'}
    ctx.run('flask run --host 127.0.0.1 --port 5000')


@task
def stopsingle(ctx):
    ctx.run('curl localhost:5000/stop')


@task
def deploycluster(ctx):
    for i in range(n):
        print(i)
        ctx.config.run.env = {'FLASK_APP': 'model_server.py', 'FLASK_ENV': 'development'}
        ctx.run('/bin/bash ./spawn_server.sh 500' + str(i + 1) + ' &')


@task
def stopcluster(ctx):
    for i in range(n):
        ctx.run('curl 127.0.0.1:500' + str(i + 1) + '/stop')
