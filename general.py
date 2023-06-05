import pandas as pd
from dateutil import parser
import yaml
from datetime import datetime


def load_config(config_file):
    with open(config_file, "r") as file:
        return yaml.safe_load(file)


def standardize_date(s, time="D"):
    s = pd.to_datetime(s.apply(parser.parse), utc=True)
    s = s.dt.tz_localize(None).dt.floor(time)
    return s


def get_timestamp():
    return datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
