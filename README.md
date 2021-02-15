Intro
=========================
**openLGD** is a Python powered library for the statistical estimation of **Credit Risk Loss** (LGD) models. It can be used both as standalone library or in a federated learning context where data remain in distinct (separate) servers

![image](static/federated_models.png)

Key Information
================
* Author: [Open Risk](http://www.openriskmanagement.com)
* License: Apache 2.0
* Development website: [Github](https://github.com/open-risk/openLGD)
* Mathematical Docs LGD Models: [Open Risk Manual](https://www.openriskmanual.org/wiki/Loss_Given_Default_Models)


**NB: This is a very early alpha release. openLGD is still in active development**


### Getting started with the demo
* Clone the repo in a local linux environment
* Install the dependencies in a virtual environment
* Fire up a number of flask servers on different shells. Check the [Spawn Cluster Script](./spawn_cluster.sh) for how to export the environment
* Run the [Controller](./federated_run.py) script to perform the demo calculation

#### Fabric based configuration
Going forward we'll use fabric and yaml to ease deployment. Check [Fabfile](./fabfile.py) for preliminary functionality

#### Dependencies
- The statistical model estimation is currently using scikit-learn / statstmodels components
- The model server is based on the python flask framework. 

The complete dependency list in the [requirements file](./requirements.txt)  

#### Startup of the model servers:
The demo Model Servers are python/flask based servers
- The model servers should startup on ports http://127.0.0.1:500X/ where X is the serial number
- You can check the server is live by pointing your browser to the port
- or by using curl from the console (curl -v http://127.0.0.1:500X/)
  
#### Model Server API endpoints: 
The general structure of the simplified API is

* GET http://127.0.0.1:500X/          API Root, indicating the server is live
* GET http://127.0.0.1:500X/start     URL to get initial locally estimated parameters (cold start)
* POST http://127.0.0.1:500X/update   URL to post current averaged parameters (warm start) 

## See Also

