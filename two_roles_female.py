from plug import TwoPointsPlug

class TwoRolesFemale:
    def plug(self, two_points_plug: TwoPointsPlug):
        if len(two_points_plug.energy_points) == 2:
            print("Successfully plugged.")
        else:
            print("Incompatible!")