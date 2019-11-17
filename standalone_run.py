# encoding: utf-8

# (c) 2019 Open Risk (https://www.openriskmanagement.com)
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
This script illustrates a basic standalone LGD model estimation workflow
It does not interact with model servers but accesses the LGD Module directly
"""

from lgdModel import lgdModel

# Number of epochs to iterate
Epochs = 10

# Initial estimate (cold start)
params = lgdModel(server=1)

# Loop over the desired number of epochs
for e in range(Epochs):
    intercept = params['intercept']
    coef = params['coefficient']
    params = lgdModel(server=1, intercept=intercept, coef=coef)
    print('Epoch: ', e, params)