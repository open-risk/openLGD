# openLGD

**openLGD** is a Python powered library for the statistical estimation of **Credit Risk Loss** (Also loss-given-default or LGD) models. 

openLGD can be used both as standalone library or in a federated analysis context where data remain in distinct (separate) servers

![image](static/federated_models.png)

## Summary Information

* Author: [Open Risk](http://www.openriskmanagement.com)
* License: Apache 2.0
* Development website: [Github](https://github.com/open-risk/openLGD)
* Mathematical Documentation of LGD Models: [Open Risk Manual](https://www.openriskmanual.org/wiki/Loss_Given_Default_Models)
* Discussion: [Open Risk Commons](https://www.openriskcommons.org/c/openlgd/19)


**NB: This is an early alpha release. openLGD is still in active development**

## Introduction

openLGD aims to support the development of both expert based and statistical [LGD Models](https://www.openriskmanual.org/wiki/LGD%20Model) 

### Standalone Mode

In *standalone mode* openLGD emulates a classic use case where, e.g., a financial institution or other credit provider aims to develop a risk quantification system on the basis of data it has in its possession.  Use cases for the standalone mode are both as intended (standalone) LGD model framework system and as a validation framework for federated applications.

The standalone mode is illustrated via the script standalone_run.py

### Federated Mode

The federated mode essentially facilitates the development of a *generic* (pooled) LGD model that applies to a wide population (which is assumed homogeneous)


#### Getting started with the federated demo

* Clone the repo in a local linux environment
* Install the dependencies in a virtual environment
* Fire up a number of flask servers on different shells. Check the [Spawn Cluster Script](./spawn_cluster.sh) for how to export the environment. This will fire up several Xterms where server output is logged
* Run the [Controller](./federated_run.py) script to perform the demo calculation

#### Fabric based configuration
Going forward we'll use fabric and yaml to ease deployment. Check [Fabfile](./fabfile.py) for preliminary functionality

#### Dependencies
- The statistical model estimation is currently using scikit-learn / statstmodels components
- The model server is based on the python flask framework. 

The complete dependency list in the [requirements file](./requirements.txt)  

#### Startup of the model servers:

The demo Model Servers are python/flask based servers
- The model servers should start up on ports http://127.0.0.1:500X/ where X is the serial number
- You can check the server is live by pointing your browser to the port
- or by using curl from the console (curl -v http://127.0.0.1:500X/)
  
#### Model Server API endpoints: 
The general structure of the simplified API is

* GET http://127.0.0.1:500X/          API Root, indicating the server is live
* GET http://127.0.0.1:500X/start     URL to get initial locally estimated parameters (cold start)
* POST http://127.0.0.1:500X/update   URL to post current averaged parameters (warm start) 

## White Papers on Federated Risk Analysis

* [White Paper: Federated Credit Systems, Part I: Unbundling The Credit Provision Business Model](https://www.openriskmanagement.com/white_paper_federated_credit_part_i_systems_unbundling_the_credit_provision_business_model/)
* [White Paper: Federated Credit Systems, Part II: Techniques for Federated Data Analysis](https://www.openriskmanagement.com/white_paper_federated_credit_systems_part_ii_techniques_for_federated_data_analysis/)