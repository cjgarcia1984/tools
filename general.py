import pandas as pd
from dateutil import parser
import yaml
from datetime import datetime
import os


def load_config(config_file):
    with open(config_file, "r") as file:
        return yaml.safe_load(file)


def standardize_date(s, time="D"):
    s = pd.to_datetime(s.apply(parser.parse), utc=True)
    s = s.dt.tz_localize(None).dt.floor(time)
    return s


def get_timestamp():
    return datetime.today().strftime("%Y-%m-%d-%H-%M-%S")


def is_same_dir(path, cwd=None):
    if cwd is None:
        cwd = os.path.dirname(os.path.realpath(__file__))
    cwd = os.path.normpath(cwd)  # Normalize the path
    repo_dir = os.path.normpath(path)  # replace with your repo's path
    return cwd == repo_dir
