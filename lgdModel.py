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

""" This module provides the statistical lgd estimation algorithms

* Currently linear regression using iterative stochastic gradient descent

"""

from sklearn import linear_model

from dataSource import dataSource


def lgdModel(server=1, choice=1, intercept=None, coef=None):

    """ Iterate a generalized linear model

    :param server: the id of the server
    :type server: integer
    :param intercept: an intercept parameter
    :type intercept: float
    :param coef: a coefficient
    :type coef: float

    Linear model fitted by minimizing a regularized empirical loss with SGD.

    SGD stands for Stochastic Gradient Descent: the gradient of the loss is
    estimated each sample at a time and the model is updated along the way with
    a decreasing strength schedule (aka learning rate).

    Parameters

        tol : float or None, default=1e-3 The stopping criterion. If it is not None, training will stop when (loss > best_loss - tol) for ``n_iter_no_change`` consecutive epochs. Convergence is checked against the training loss or the validation loss depending on the `early_stopping` parameter.

        max_iter : int, default=1000 The maximum number of passes over the training data (aka epochs). It only impacts the behavior in the ``fit`` method, and not the :meth:`partial_fit` method.

        verbose : int, default=0 The verbosity level.

        warm_start : bool, default=False
        When set to True, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution.

        Repeatedly calling fit or partial_fit when warm_start is True can result in a different solution than when calling fit a single time because of the way the data is shuffled. If a dynamic learning rate is used, the learning rate is adapted depending on the number of samples already seen. Calling ``fit`` resets this counter, while ``partial_fit``  will result in increasing the existing counter.

        early_stopping : bool, default=False
            Whether to use early stopping to terminate training when validation score is not improving. If set to True, it will automatically set aside a fraction of training data as validation and terminate training when validation score returned by the `score` method is not improving by at least `tol` for `n_iter_no_change` consecutive epochs.

    """

    # A linear LGD model to be estimated iteratively
    clf = linear_model.SGDRegressor(tol=None, max_iter=1, verbose=0, warm_start=False,
                                    early_stopping=False)
    # The server ID
    n = server

    # Fetch data from desired datasource
    # choice = 1 - from local file
    # choice = 2 - from database via REST API

    df = dataSource(n, choice)

    # Extract explanatory and target variables
    # X is target variable (E.g., Loss Severity or LGD)
    X = df[['X']]
    # y is dataframe of explanatory variables
    y = df['Y']

    # Estimate model (initial or update mode)
    if intercept is None or coef is None:
        clf.fit(X, y)
    else:
        clf.fit(X, y, intercept_init=intercept, coef_init=coef)

    # Return the current parameter estimates
    fitted_params = {'intercept': clf.intercept_[0], 'coefficient': clf.coef_[0]}
    return fitted_params
