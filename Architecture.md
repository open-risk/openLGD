# Core algorithm modules

* standalone version of models / algorithms
* forms the benchmark implementation against which federate versions are checked 

# Standard estimation node

flask server that

* has access to a local data store
* implements the standalone version of the algorithm

# Coordinating node

flask server that

* stores intermediate parameter estimation results
* sends current parameters to estimation nodes
* collects updated parameters from estimation nodes
