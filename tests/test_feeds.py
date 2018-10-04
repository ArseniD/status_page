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
          "id": 1,
          "time": "2018-09-04 06:00:16",
          "name": "Project price update U - Uploaded September 04, 2018 06:00:16 AM"
        },

        {
          "id": 2,
          "time": "2018-09-04 05:25:04",
          "name": "Project price update EU - Uploaded September 04, 2018 05:25:04 AM"
        },

        {
          "id": 3,
          "time": "2018-09-04 02:00:50",
          "name": "Project price update AU - Uploaded September 04, 2018 02:00:50 AM"
        },

        {
          "id": 4,
          "time": "2018-09-04 03:30:04",
          "name": "DMM feed - Uploaded September 04, 2018 03:30:04 AM"
        },

        {
          "id": 5,
          "time": "2018-09-04 02:00:47",
          "name": "DMM non-product feed - Uploaded August 24, 2018 02:00:08 AM"
        }
    ]}
    """)
    log_file.close()
    feeds.feed_check(log_file.name)
    url = "http://localhost/api/v1/incidents"
    response = requests.request("GET", url)
    assert json.loads(response.text)["meta"]["pagination"]["count"] == 0
