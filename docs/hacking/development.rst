GitLight Development
====================

There should be nothing more exciting than developing quality code.

Prerequisites:

- Read our `Code of Conduct`_
- Read our `Contribution Rules`_

.. _Code of Conduct: https://github.com/gitlight/gitlight/blob/master/CODE_OF_CONDUCT.md
.. _Contribution Rules: https://github.com/gitlight/gitlight/blob/master/.github/CONTRIBUTING.md

Vagrant Dev
-----------

Using vagrant provides a convenient method to bootstrap a new development
environment. It ensures a clean development environment where tests can easily
be run and documentation can easily be built.

Using Virtualbox
++++++++++++++++

Virtualbox is a simple virtualization tool that works across different platforms.
Linux users can [download a package or add a repository]
(https://www.virtualbox.org/wiki/Linux_Downloads) to let their package manager
keep virtualbox up to date. Virtualbox also supports [Windows, OSX, and Solaris]
(https://www.virtualbox.org/wiki/Downloads).

Installing the tools (on Linux):

    apt-get install vagrant virtualbox-5.2  # or newer

In order for vagrant to work with virtualbox virtual machines, the extension pack
needs to be installed:

- Visit the [virtualbox download](https://www.virtualbox.org/wiki/Downloads) page
- Under ``VirtualBox Extension Pack``, download via ``All supported platforms``
- Open virtualbox, as root
- File > Preferences > Extensions
- Click ``+`` and select the downloaded file
- Click Install, READ the license, choose your fate
- Close this virtualbox instance (since it's root)

Run with:

    vagrant up --provider virtualbox

Log in to instance with:

    vagrant ssh

Test instances can be accessed at <http://localhost:8080/>.

Destroy with:

    vagrant destroy

Using LXC
+++++++++

# todo

Python Virtualenv
-----------------

.. note:: When vagrant is used, this section is part of the bootstrap process
          and can be skipped.

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

Changes can now be made on the ``my-changes`` branch.

When submitting a Pull Request, make sure to check the diff. If the wrong branch
was selected, the changeset can be much larger than expected.

Note: Only bug fixes will be backported to supported release branches. New features
must be submitted to ``master``.

Running GitLight
----------------

To run gitlight:

    make run

This will run a local server on port 5000:

    http://127.0.0.1:5000/
