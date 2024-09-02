from plug import TwoPointsPlug, ThreePointsPlug

class ThreeToTwoPointsPlugAdapter(TwoPointsPlug):
    def __init__(self, three_points_plug: ThreePointsPlug):
        self.plug = three_points_plug

        # adapting energy points to fit 2
        self.energy_points = [
            self.plug.energy_points[0],
            self.plug.energy_points[1],
        ]
    