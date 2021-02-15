# encoding: utf-8

# (c) 2019 - 2021 Open Risk (https://www.openriskmanagement.com)
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

""" This module provides the statistical lgd estimation algorithms

* Currently linear regression using iterative stochastic gradient descent

"""

import pandas as pd
import requests
from sklearn import linear_model


def dataSource(server=1, choice=1):
    # TODO remove file / url path hardwiring
    if choice == 1:
        # Load data from local storage
        Data_Location = './server_dirs/' + str(server) + '/'
        df = pd.read_csv(Data_Location + 'regression_data.csv')
        return df
    elif choice == 2:
        # Load data from local openNPL database
        # GET request to appropriate endpoint
        data_server_url = "http://localhost:800" + str(server) + "/api/npl_data/counterparties"
        # Returns json object with counterparty catalog
        # query individual points to get data
        # convert data to dataframe
        data_list = []
        res = requests.get(data_server_url)
        entries = res.json()
        for entry in entries:
            data_url = entry['link']
            res2 = requests.get(data_url)
            data = res2.json()
            data_list.append((data['current_assets'], data['cash_and_cash_equivalent_items']))
        df = pd.DataFrame(data_list, columns=['X', 'Y'])
        return df


def lgdModel(server=1, intercept=None, coef=None):
    """ Iterate a generalized linear model

    :param server: the id of the server
    :type server: integer
    :param intercept: an intercept parameter
    :type intercept: float
    :param coef: a coefficient
    :type coef: float

    """

    clf = linear_model.SGDRegressor(tol=None, max_iter=1, verbose=0, warm_start=False,
                                    early_stopping=False)
    # The server ID
    n = server

    # Fetch data
    # choice = 1 - from local file
    # choice = 2 - from database via REST API

    df = dataSource(n, 2)

    # Extract explanatory and target variables
    X = df[['X']]
    y = df['Y']

    # Estimate model (initial or update mode)
    if intercept is None or coef is None:
        clf.fit(X, y)
    else:
        clf.fit(X, y, intercept_init=intercept, coef_init=coef)

    # Return the current parameter estimates
    fitted_params = {'intercept': clf.intercept_[0], 'coefficient': clf.coef_[0]}
    return fitted_params
