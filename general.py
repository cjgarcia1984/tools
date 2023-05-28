import pandas as pd
from dateutil import parser


def standardize_date(s, time="D"):
    s = pd.to_datetime(s.apply(parser.parse), utc=True)
    s = (
        s.dt.tz_localize(None).dt.floor(time)
    )
    return s
