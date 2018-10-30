status_page
========

Creates incident normally contains information about the state of a particular component on the cashet server based on “daily_check” log file.

Preparing for Development
--------------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone https://github.com/ArseniD/status_page.git``
3. Fetch development dependencies: ``make install``
4. Install and run cashet locally via docker ``https://github.com/CachetHQ/Docker``
5. Get cashet token value and past it to token TOKEN variable in feeds.py module

Usage
-------

Takes a path to a log file, read a given log and creates an incident based on the current state of the daily check components.

Path Example w/ log path:

::

        $ status_page --file /home/user/daily_check.log


Example of daily_check log file:

::

    {
      "feeds": [
        {
          "time": "2018-09-04 06:00:16",
          "name": "Project price update US - Uploaded September 04, 2018 06:00:16 AM Deployed"
        },

        {
          "time": "2018-09-04 05:25:04",
          "name": "Project price update EU - Uploaded September 04, 2018 05:25:04 AM Deployed"
        },

        {
          "time": "2018-09-04 02:00:50",
          "name": "Project price update AS - Uploaded September 04, 2018 02:00:50 AM Deployed"
        },

        {
          "time": "2018-09-04 03:30:04",
          "name": "DMM feed - Uploaded September 04, 2018 03:30:04 AM Deployed"
        },

        {
          "time": "2018-09-04 02:00:47",
          "name": "DMM non-product feed - Uploaded August 04, 2018 02:00:08 AM Deployed"
        },

        {
          "time": "2018-09-04 03:00:47",
          "name": "Project Project catalogue - Uploaded August 04, 2018 03:00:08 AM Deployed"
        }
      ]
    }


Running Tests
-----------------

Run tests locally using ``make`` if virtualenv is active:

::

        $ make

If virtualenv isn't active then use:

::

        $ pipenv run make
