<!-- ## 1. Describe the Problem -->

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were

## 2. Design the Class System

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Car(front_left_tire, front_right_tire, back_right_tire, back_left_tire) │
│                                                                         │
│ - tires[2][2]                                                           │
│ - get_details()                                                         │
└───────────┬─────────────────────────────────────────────────────────────┘
            │
            │ owns a list of
            ▼
┌──────────────────────────────┐
│ Tire()                       │
│                              │
│ - pressure_history           │
│ - depth_history              │
│ - current_pressure           │
│ - current_depth              │
│ - record_pressure(pressure)  │
│ - record_tread_depth(depth)  │
└──────────────────────────────┘
            │
            │ owns historical lists of
            ▼
┌──────────────────────────────┐
│ TireReading(value, timestamp)│
│                              │
└──────────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Car():
    # User-facing properties

    def __init__(self):
        # parameters:
        # None
        # Side effects:
        # Initialises self.tires as a two dimensional array with 4 tires in the format [2][2]
        pass

    def get_details(self) -> list[dict]:
        # parameters
        # None
        # Returns
        # Four element array countaining dictionaries with the details of each tire

class Tire():
    def __init__():
        # Parameters:
        # None
        # Side effects
        # Initialises pressure history and depth history as empty arrays
        # Initialises current pressure and current depth as None

    def record_pressure(pressure: float, timestamp):
        # parameters
        # pressure reading as a float
        # timestamp as a date time
        # Returns
        # None
        # Side effects
        # Appends the current pressure value to the pressure history
        # Sets the new pressure value as a new TireReading object()

    def record_tread_depth(depth: float, timestamp):
        # parameters
        # depth reading as a float
        # timestamp as a date time
        # Returns
        # None
        # Side effects
        # Appends the current depth value to the depth history
        # Sets the new depth value as a new TireReading object()

class TireReading():
    def __init__(reading, timestamp):
        # Parameters
        # Reading value as a number
        # Time stamp as a date time
        # Side effects
        # Sets self.reading to reading
        # Sets self.timestamp to timestamp
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

def test_add_reading_to_tire():
    tire = Tire()
    tire.add_pressure(28, Date(12, 05, 2007))
    tire.add_tread_depth(5, Date(1, 05, 2007))

    pressure_reading = tire.current_pressure
    assert pressure_reading.reading == 28
    assert pressure_reading.timestamp == DateTime(12,05,2007)

    tread_depth_reading = tire.current_depth
    assert tread_depth_reading.reading == 5
    assert tread_depth_reading.timestamp == Date(1, 05, 2007)

def test_add_historical_reading_to_tire():
    tire = Tire()

    pressures_dates = [DateTime(12, 08, year) for year in range(2010, 2025)]

    for date in pressure_dates():
        tire.add_pressure(28, date)

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
            tire.add_pressure(pressure, DateTime(6,10,2026))
            tire.add_tread_depth(depth, DateTime(6,10,2026))
            depth += 5
            pressure += 20

    details = car.get_details():


    assert details[0].position == "front left"
    assert details[0].pressure.reading == 20
    assert details[0].depth.reading == 5

    assert details[0].position == "front right"
    assert details[0].pressure.reading == 40
    assert details[0].depth.reading == 10

    assert details[0].position == "back left"
    assert details[0].pressure.reading == 60
    assert details[0].depth.reading == 15

    assert details[0].position == "back right"
    assert details[0].pressure.reading == 80
    assert details[0].depth.reading == 20



```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

def test_tire_reading():
    reading = TireReading(5, DateTime(25, 5, 2020))

    assert reading.reading == 5
    assert reading.timestamp == DateTime(25, 5, 2020)



```
