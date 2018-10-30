import pytest
import tempfile
import os
import re
import time

from status_page import helpers


@pytest.fixture(scope="session")
def _dir_with_files(tmpdir_factory):
    """
    Create the `logs` folder in the system tmpdir and place 4 logs inside,
    where `feed.log.2018-10-24` is the latest log

    return: path to the `logs` folder
    """
    temp_dir = tmpdir_factory.mktemp("logs", numbered=False)
    temp_dir.join('feed.log').write("content")
    time.sleep(1)
    temp_dir.join('feed.log.2018-10-22').write("content")
    time.sleep(1)
    temp_dir.join('feed.log.2018-10-23').write("content")
    time.sleep(1)
    temp_dir.join('feed.log.2018-10-24').write("content")
    return str(temp_dir)


def test_load():
    """
    `helpers.load` takes a path to a file and parses it as JSON
    """
    log_file = tempfile.NamedTemporaryFile(delete=False)
    log_file.write(b"""
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
    """)
    log_file.close()
    log_data = helpers.load(log_file.name)
    assert log_data['feeds'][0]['name'] == "Project price update US - Uploaded September 04, 2018 06:00:16 AM Deployed"
    assert log_data['feeds'][1]['name'] == "Project price update EU - Uploaded September 04, 2018 05:25:04 AM Deployed"
    assert log_data['feeds'][2]['name'] == "Project price update AS - Uploaded September 04, 2018 02:00:50 AM Deployed"
    assert log_data['feeds'][3]['name'] == "DMM feed - Uploaded September 04, 2018 03:30:04 AM Deployed"
    assert log_data['feeds'][4]['name'] == "DMM non-product feed - Uploaded August 04, 2018 02:00:08 AM Deployed"
    assert log_data['feeds'][5]['name'] == "Project Project catalogue - Uploaded August 04, 2018 03:00:08 AM Deployed"


def test_get_latest_log(_dir_with_files):
    """
    `helpers.get_latest_log` takes a path to a directory with logs and
    return a path to the latest log
    """
    assert helpers.get_latest_log(_dir_with_files) == _dir_with_files + '/feed.log.2018-10-24'
