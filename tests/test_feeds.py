import pytest
import requests
import tempfile
import json

from status_page import feeds, helpers


def test_feed_check():
    """
    `feeds.feed_check` takes a path to a file and parses it as JSON
    then check feeds and incidents out on the local cashet server.
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
    feeds.feed_check(log_file.name)
    url = "http://localhost/api/v1/incidents"
    response = requests.request("GET", url)
    assert json.loads(response.text)["meta"]["pagination"]["count"] == 0
