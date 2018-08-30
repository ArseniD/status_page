status_page
========

Creates incident normally contains information about the state of a particular component on the cashet server based on “daily_check” log file.

Preparing for Development
--------------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone https://github.com/ArseniD/status_page.git``
3. Fetch development dependencies: ``make install``

Usage
-------

Takes a path to log, read a given log and creates an event or incident based on the current state of the components.

Path Example w/ log path:

::

        $ status_page --file /home/user/daily_check.log


Example inventory JSON file:

::

   TODO

Running Tests
-----------------

Run tests locally using ``make`` if virtualenv is active:

::

        $ make

If virtualenv isn't active then use:

::

        $ pipenv run make
