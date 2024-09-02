from two_roles_female import TwoRolesFemale
from plug import ThreePointsPlug
from plug_adapter import ThreeToTwoPointsPlugAdapter

if __name__ == '__main__':
    female_input = TwoRolesFemale()
    tree_points_plug = ThreePointsPlug()
    female_input.plug(ThreeToTwoPointsPlugAdapter(tree_points_plug))
