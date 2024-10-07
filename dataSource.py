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

""" This module provides provides a data source for LGD data.

* Under choice = 1, data are assumed available in parametrically named local directories (/server_dirs/X/datafile) where X is the server ID
* Under choice = 2, data are assumed available in parametrically named URL's from data server API's (serverurl/X/api/npl_data/counterparties)

"""

import pandas as pd
import requests


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
