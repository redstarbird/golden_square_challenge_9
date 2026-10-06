from lib.car import *
from lib.tire import *
from lib.tire_reading import *
from datetime import datetime

def test_add_reading_to_tire():
    tire = Tire()
    tire.record_pressure(28, datetime(2007, 5, 12))
    tire.record_tread_depth(5, datetime(2007, 5, 1))

    pressure_reading = tire.current_pressure
    assert pressure_reading.reading == 28
    assert pressure_reading.timestamp == datetime(2007, 5, 12)

    tread_depth_reading = tire.current_depth
    assert tread_depth_reading.reading == 5
    assert tread_depth_reading.timestamp == datetime(2007, 5, 1)

def test_add_historical_reading_to_tire():
    tire = Tire()

    pressures_dates = [datetime(year, 8, 12,) for year in range(2010, 2025)]

    for date in pressures_dates:
        tire.record_pressure(28, date)

    pressures = tire.pressure_history

    for i in range(len(pressures)):
        assert pressures[i].timestamp == pressures_dates[i]


def test_initialise_car():
    car = Car()

    assert len(car.tires) == 2
    assert len(car.tires[0]) == 2

    for i in car.tires:
        for j in i:
            assert isinstance(j, Tire)

def test_car_get_details():
    car = Car()

    pressure = 20
    depth = 5
    for side in car.tires:
        for tire in side:
            tire.record_pressure(pressure, datetime(2026, 10, 6))
            tire.record_tread_depth(depth, datetime(2026, 10, 6))
            depth += 5
            pressure += 20

    details = car.get_details()


    assert details[0]['position'] == "front left"
    assert details[0]['pressure'].reading == 20
    assert details[0]['depth'].reading == 5

    assert details[1]['position'] == "front right"
    assert details[1]['pressure'].reading == 40
    assert details[1]['depth'].reading == 10

    assert details[2]['position'] == "back left"
    assert details[2]['pressure'].reading == 60
    assert details[2]['depth'].reading == 15

    assert details[3]['position'] == "back right"
    assert details[3]['pressure'].reading == 80
    assert details[3]['depth'].reading == 20