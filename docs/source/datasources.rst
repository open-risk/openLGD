Data Sources
=========================

This module provides provides a data source for LGD data.

* Under choice = 1, data are assumed available in parametrically named local directories (/server_dirs/X/datafile) where X is the server ID
* Under choice = 2, data are assumed available in parametrically named URL's from data server API's (serverurl/X/api/npl_data/counterparties)


Data Format
--------------------------

The data format is a CSV file where:

* the first column is the target variable and all subsequent columns are explanatory variables
* each row represents a single unique observation of realized loss / recovery