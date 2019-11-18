Intro
=========================
openLGD is a Python framework for the statistical estimation of Credit Risk Loss Given Default models. 
It can be used both as standalone library and in a _federated learning_ context where data remain in distinct 
(separate) servers. 

**NB: The current release is a preliminary proof-of-concept release.**

![image](static/federated_models.png)

Key Information
================
* Author: [Open Risk](http://www.openriskmanagement.com)
* License: Apache 2.0
* Mathematical Documentation: [Open Risk Manual](https://www.openriskmanual.org/wiki/Loss_Given_Default_Models)
* Development website: [Github](https://github.com/open-risk/openLGD)


#### Dependencies
- The statistical model estimation is currently using scikit-learn / statstmodels components
- The model server is based on the python flask framework
- The federated demo assumes a linux environment (including xterm) 

The complete dependency list in the [requirements file](./requirements.txt)  


### Explore the federated demo
Currently the demo is setup for a linux environment. Step by step instructions are [given here](./Federated_Demo.md).


### Get involved
Get in touch if you would like to be involved in the further development or use of openLGD as a standalone or
federated framework


