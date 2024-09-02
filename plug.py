from energy_point import EnergyPoint

class TwoPointsPlug:
    def __init__(self):
        self.energy_points = [
            EnergyPoint('positive'),
            EnergyPoint('negative'),
        ]

class ThreePointsPlug:
    def __init__(self):
        self.energy_points = [
            EnergyPoint('positive'),
            EnergyPoint('negative'),
            EnergyPoint('grounded'),
        ]
