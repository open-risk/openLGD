Model Server
=========================

This module provides a model server that has local access to distributed data sources

Each federated model server makes three endpoints available
1) GET localhost:/          API Root, indicating the server is live
2) GET localhost:/start     URL to get initial locally estimated parameters (cold start)
3) POST localhost:/update   URL to post current averaged parameters (warm start)