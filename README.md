# Adapter

This project implements a use case for a Design Pattern, the Singleton. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/adapter).

## What it is?

Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

## Project

This design pattern is pretty simple, we just need a two interface that do not communicate well one each other. So let's create a classic problem for Brazilian people, this one:

![tomada](/images/macho.webp)

![tomada](/images/femea.jpeg)

First of all let's create the client code:

```python
if __name__ == '__main__':
    female_input = TwoRolesFemale()
    tree_points_plug = ThreePointsPlug()
    female_input.plug(ThreeToTwoPointsPlugAdapter(tree_points_plug))
```

This is what we are trying to implement, let's create the classes. First the Female input:

```python
from plug import TwoPointsPlug

class TwoRolesFemale:
    def plug(self, two_points_plug: TwoPointsPlug):
        if len(two_points_plug.energy_points) == 2:
            print("Successfully plugged.")
        else:
            print("Incompatible!")
```

Now let's create the plugs:

```python

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
```

And finally, the adapter:

```python
from plug import TwoPointsPlug, ThreePointsPlug

class ThreeToTwoPointsPlugAdapter(TwoPointsPlug):
    def __init__(self, three_points_plug: ThreePointsPlug):
        self.plug = three_points_plug

        # adapting energy points to fit 2
        self.energy_points = [
            self.plug.energy_points[0],
            self.plug.energy_points[1],
        ]
    
```

Of course, this is just a representation, we are ignoring the "grounded" energy point and using only "positive" and "negative" energy points. When the code is executed:

```bash
python main.py
Successfully plugged.
```

If we remove the adapter from *main.py* this happens:

```python
if __name__ == '__main__':
    female_input = TwoRolesFemale()
    tree_points_plug = ThreePointsPlug()
    female_input.plug(tree_points_plug)
```

```bash
python main.py
Incompatible!
```

Thanks for reading.
