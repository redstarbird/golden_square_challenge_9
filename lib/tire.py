from lib.tire_reading import TireReading

class Tire():
    def __init__(self):
        self.current_pressure: TireReading = None
        self.current_depth: TireReading = None
        self.pressure_history: list[TireReading] = []
        self.depth_history: list[TireReading] = []


    def record_pressure(self,pressure: float, timestamp):
        if self.current_pressure != None:
            self.pressure_history.append(self.current_pressure)

        self.current_pressure = TireReading(pressure, timestamp)

        
        

    def record_tread_depth(self,depth: float, timestamp):
        if self.current_depth != None:
            self.depth_history.append(self.current_depth)

        self.current_depth = TireReading(depth, timestamp)