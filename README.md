Google Tests
============================

This repository is being used as a project to learn about automated testing through writing our own page objects models and tests. We are not affiliated with Google.

Getting set up
-------------
It's easy to get set up: just 2 pieces of software to install and in 5 command lines you'll be running the tests!

### Install Python
If you don't already have it installed, please install [Python 2.6]
[Python 2.6]: http://www.python.org/download/releases/2.6.6/

### Cloning the test repository with Git

After you have installed [Git] you will need to clone the project to your hard drive. From your workspace directory run this command which will copy (clone) the project to your hard drive

git clone --recursive git://github.com/mozilla/PROJECT_NAME.git
[Git]: http://en.wikipedia.org/wiki/Git_%28software%29

### Installing Python packages
You will need to install Selenium, py.test, unittestzero and some other project specific packages. Fortunately `pip` makes it easy to install all of these in one step. Let's start by installing pip:

sudo easy_install pip

Now using pip we'll install the packages we need (which are listed in requirements.txt)

pip install -Ur requirements.txt --use-mirrors

__Optional/Intermediate level__

##### Virtual Environments
The step above installs the packages globally on your operating system. Using `virtualenv` you can sandbox Python packages into virtual environments for each Mozilla project you work on. Follow our [Virtual Env guide] to get a virtual environment up and running. We recommend this practice.
[Virtual Env guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Automation/Virtual_Environments

Running Tests
-------------

### Selenium
Once the above prerequisites have been met, you can run the tests using the
following command:

py.test --driver=firefox

This command will locate your Firefox install, load it and run the tests against it.

For other possible options, type `py.test --help` or view the [readme].
[readme]: https://github.com/davehunt/pytest-mozwebqa/blob/master/README.md

License
-------
This software is licensed under the [MPL] 2.0:

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/
