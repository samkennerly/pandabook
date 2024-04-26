"""
Constants and convenience functions.
"""
from pathlib import Path

from numpy import random
from pandas import Categorical, DataFrame, Series, read_csv, to_datetime


REPO = Path(__file__).resolve().parent.parent
DATADIR = REPO / "data"


def afew(data, n=5):
    """DataFrame view: Distinct random rows from a DataFrame."""
    return data.loc[random.choice(data.index, size=n, replace=False)].copy()
