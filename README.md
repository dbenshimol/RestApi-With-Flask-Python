![start with why](https://img.shields.io/pypi/l/tweepy)
![](https://img.shields.io/pypi/l/pandas)
[![Documentation Status](http://img.shields.io/badge/docs-v3.9.0-brightgreen.svg?style=flat)](http://docs.tweepy.org)
[![Version](http://img.shields.io/pypi/v/tweepy.svg?style=flat)](https://pypi.org/project/tweepy/)
![Python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue)
# Build REST APIs with Python, Flask, Flask-RESTful, and Flask-SQLAlchemy
 Using Flask and popular extensions Flask-RESTful, Flask-JWT, and Flask-SQLAlchemy implement via technologies Git, Heroku, and nginx.

 Connect web or mobile applications to databases and servers via REST APIs

 Create secure and reliable REST APIs which include authentication, logging, caching, and more
 



# But what is a REST API anyway?
 Put simply, a REST API is an application that accepts data from clients and returns data back. With the data, it can do many things. For example, a REST API app that accepts text data from the client, processes it and stores it in a database, and then returns some data back so the client can show something to the user.


Flask: 
======
###  Installing relevant Libraries
Its recommend using the latest version of Python 3. Flask supports Python 3.5 and newer, Python 2.7, and PyPy.

```
pip install Flask
```


Virtual environments:
======
Use a virtual environment to manage the dependencies for your project, both in development and in production.

What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one project can break compatibility in another project.

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python 3 comes bundled with the venv module to create virtual environments. If you’re using a modern version of Python, you can continue on to the next section.

## Create an environment

#### Create a project folder and a venv folder within:
```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```
## Activate the environment
Before you work on your project, activate the corresponding environment:
```
$ . venv/bin/activate
```




