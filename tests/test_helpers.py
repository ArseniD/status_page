import pytest
import tempfile

from status_page import helpers


def test_load():
    """
    `helpers.load` takes a path to a file and parses it as JSON
    """
    log_file = tempfile.NamedTemporaryFile(delete=False)
    log_file.write(b"""
    {
      "feeds": [
        {
          "id": 1,
          "time": "2018-09-04 06:00:16",
          "name": "Project price update US - Uploaded September 04, 2018 06:00:16 AM"
        },

        {
          "id": 2,
          "time": "2018-09-04 05:25:04",
          "name": "Project price update EU - Uploaded September 04, 2018 05:25:04 AM"
        },

        {
          "id": 3,
          "time": "2018-09-04 02:00:50",
          "name": "Project price update AS - Uploaded September 04, 2018 02:00:50 AM"
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
    log_data = helpers.load(log_file.name)
    assert log_data['feeds'][0]['name'] == "Project price update US - Uploaded September 04, 2018 06:00:16 AM"
    assert log_data['feeds'][1]['name'] == "Project price update EU - Uploaded September 04, 2018 05:25:04 AM"
    assert log_data['feeds'][2]['name'] == "Project price update AS - Uploaded September 04, 2018 02:00:50 AM"
    assert log_data['feeds'][3]['name'] == "DMM feed - Uploaded September 04, 2018 03:30:04 AM"
    assert log_data['feeds'][4]['name'] == "DMM non-product feed - Uploaded August 24, 2018 02:00:08 AM"
