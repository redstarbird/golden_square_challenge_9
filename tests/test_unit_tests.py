from lib.tire_reading import *
from datetime import datetime

def test_tire_reading():
    reading = TireReading(5, datetime(25, 5, 2020))

    assert reading.reading == 5
    assert reading.timestamp == datetime(25, 5, 2020)
