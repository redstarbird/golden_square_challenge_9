from lib.tire_reading import *
from datetime import datetime

def test_tire_reading():
    reading = TireReading(5, datetime(2020, 5 ,25))

    assert reading.reading == 5
    assert reading.timestamp == datetime(2020, 5 ,25)
