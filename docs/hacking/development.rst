GitLight Development
====================

There should be nothing more exciting than developing quality code.

Prerequisites:

- Read our `Code of Conduct`_
- Read our `Contribution Rules`_

.. _Code of Conduct: https://github.com/gitlight/gitlight/blob/master/CODE_OF_CONDUCT.md
.. _Contribution Rules: https://github.com/gitlight/gitlight/blob/master/.github/CONTRIBUTING.md

Python Virtualenv
-----------------

The cleanest way to handle dependencies during development is with virtualenv.

Create a py3 venv with ``python3-venv``:

    python3 -m venv ~/.venv

Activate it using:

    . ~/.venv/bin/activate

Now you can install python modules through pip without modifying the rest of
the system. Some of these installations will require compiling source code. The
most common requisites are ``build-essential`` and ``python3-dev``.

To install all dependencies, change your working directory to gitlight and run:

    pip3 -r requirements/all.txt

Other requirements files exist for various purposes.

Making Changes
--------------

Making changes is best done in a personal repository with a dedicated branch.

If you forked gitlight on github, then the process would look similar to this:

    git clone git@github.com/username/gitlight
    cd gitlight

    git remote add upstream https://github.com/gitlight/gitlight
    git fetch --tags upstream

    git branch -b my-changes upstream/master

Changes can now be mane on the ``my-changes`` branch.

When submitting a Pull Request, make sure to check the diff. If the wrong branch
was selected, the changeset can be much larger than expected.

Note: Only bug fixes will be backported to supported release branches. New features
must be submitted to ``master``.

Running GitLight
----------------

To run gitlight:

    cd /path/to/gitlight
    export FLASK_APP=gitlight
    export FLASK_ENV=development
    flask run

This will run a local server on port 5000:

    http://127.0.0.1:5000/
