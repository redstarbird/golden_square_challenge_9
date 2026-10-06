from lib.tire import Tire
from lib.tire_reading import TireReading

class Car():
    # User-facing properties

    def __init__(self):
        self.tires = [[Tire(), Tire()],[Tire(), Tire()]]

    def get_details(self) -> list[dict]:
        details_array = []
        position_names = ['front left', 'front right', 'back left', 'back right']

        i = 0
        for side in self.tires:
            for tire in side:
                tire_dict = {'position': position_names[i], 'pressure': tire.current_pressure, 'depth': tire.current_depth}
                details_array.append(tire_dict)
                i += 1
            

        return details_array