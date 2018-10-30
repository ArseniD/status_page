import glob
import json
import os


def load(path):
    """
    Given a path to the log file

    return: json data
    """
    with open(path) as file:
        return json.load(file)


def get_latest_log(path):
    """
    Given a path to the log dir

    return: the lates log file
    """
    files = glob.glob(path + '/feed.log.[0-9]*')
    files.sort(key=os.path.getctime)
    return files[-1]
