import datetime
from unittest.mock import Mock
import unittest

# Save a couple of test days
year1 = datetime.datetime(year=2019, month=1, day=1)
year2 = datetime.datetime(year=2020, month=1, day=1)

def is_leap_year():
    today = datetime.datetime.today()
    return today.year % 400 == 0 or (today.year % 4 == 0 and today.year % 100 != 0)

# Mock datetime to control today's date
datetime = Mock()

datetime.datetime.today.return_value = year1
assert not is_leap_year()
datetime.datetime.today.return_value = year2
assert is_leap_year()
