GitLight
========

GitLight is a simple/lightweight collaboration tool built on top of Gitolite3.

<!--<p align="center"><img src="https://raw.githubusercontent.com/gitlight/gitlight/master/app/static/images/gitlight-logo.png" width="128px"><p>-->

![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
[![GitHub Issues](https://img.shields.io/github/issues/gitlight/gitlight.svg)](https://github.com/gitlight/gitlight/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![Documentation](https://readthedocs.org/projects/gitlight/badge/?version=latest)](https://docs.gitlight.io)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://opensource.org/licenses/gpl-3.0.html)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/52fca2eb2dcb4039aacca674133eb4cd)](https://www.codacy.com/app/MTecknology/gitlight?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gitlight/gitlight&amp;utm_campaign=Badge_Grade)

Running GitLight
----------------

Prerequisites:

-   Gitolite3 Installed/Configured

GitLight is meant to be run behind an application server, such as uWSGI. The
documentation provides information for running GL behind uWSGI and Nginx.

A development version of the application can be run using:

    $ python3 manage.py runserver

Custom Configuration
--------------------

The configuration files provided in this repository are intended for testing and
providing information. Only these two files are tracked by version control.

Test Suite
----------

This application contains unit tests, which can be executed with the following command:

    $ python3 manage.py test

Requirements
------------

pip:

    $ pip install -r requirements/base.txt
    $ package_manager install git gitolite3

debian:

    $ apt-get install python-flask python-flask-babel python-flask-api python-flask-bcrypt \
                      python-flask-restful python-flask-sqlalchemy python-flask-httpauth \
                      python-flask-sockets \
                      git gitolite3

Scope
-----

GitLight is meant to be a simple and lightweight tool to make collaboration with
gitolite3 easy and enjoyable. Wiki, Issues, and Project features are out of scope
for this project. Although, it may be possible to write a pluggable interface to
include additional features.

Primary Features:

-   [ ] Authentication:

    -   [ ] Username/Password
    -   [ ] Browser Certificate
    -   [ ] Honor Gitolite ACL

-   [ ] View Repository:

    -   [ ] List Code
    -   [ ] Render README
    -   [ ] Render Source
    -   [ ] Support Git Blame
    -   [ ] View Commit History
    -   [ ] View Commit Diff

-   [ ] Pull Requests:

    -   [ ] Notify Users
    -   [ ] Discussion Support
    -   [ ] View Diff
    -   [ ] Reviewer Support
    -   [ ] CI/CD Support

-   [ ] Misc:

    -   [ ] Unit/Integration Tests
    -   [ ] Internationalization Support
    -   [ ] Accurate Usage Documentation
    -   [ ] Automated API Documentation
    -   [ ] Modular Design (Support Plugins)
    -   [ ] Simple Template Support
