from .helpers import load
import requests
import datetime

URL = "http://localhost/api/v1/incidents"

TOKEN = "1Jd0qjPdwiaBkb6F32Ch"

HEADERS = {"X-Cachet-Token": TOKEN,
           "Content-Type": "application/json"}

FEEDS = ["Project price update US",
         "Project price update EU",
         "Project price update AS",
         "DMM feed",
         "DMM non-product feed",
         "Project Project catalogue"]


def feed_check(log_data):
    """
    Create an incident with description on the cashet server
    if some feed was not found in `log_data` file.
    """
    data = load(log_data)
    feed_list = [feed['name'] for feed in data['feeds']]
    for feed in FEEDS:
        if feed not in str(feed_list):
            payload = "{\"name\":\"%s is missing\",\"message\":\"There is no %s\",\"status\":1,\"visible\":1}" % (feed, feed)
            response = requests.request("POST", URL, data=payload, headers=HEADERS)
            print(response.text)
