from variable import Variable
from systems import (
    Feeding,
    FishHealthMonitoring,
    EnvironmentalControlMonitoring,
    WaterFiltering,
    Lighting,
)
import random

# Central Control Unit (CCC)
# Use terminal as console?


class CCC:
    def __init__(self):
        # Initialize systems
        self.feeding = Feeding()
        self.fish_health_monitoring = FishHealthMonitoring()
        self.environment_control_monitoring = EnvironmentalControlMonitoring()
        self.waterfiltering = WaterFiltering()
        self.lighting = Lighting()
        self.all_systems = [
            self.feeding,
            self.fish_health_monitoring,
            self.environment_control_monitoring,
            self.waterfiltering,
            self.lighting,
        ]

    # Randomise all variables
    def randomiseVariables(self):
        for system in self.all_systems:
            for var in system.getVariables():
                var.set_value(random.choice([True, False]))

    # Print all variables state
    def printVariables(self):
        for system in self.all_systems:
            print(f"\n*** {system.name} ***")
            for var in system.getVariables():
                print(var)

    # Set all variables to True
    def setVariablesTrue(self):
        for system in self.all_systems:
            for var in system.getVariables():
                var.set_value(True)

    # Set all variables to False
    def setVariablesFalse(self):
        for system in self.all_systems:
            for var in system.getVariables():
                var.set_value(False)

    # Test systems and variables
    def testSystems(self):
        # Print all variables
        self.printVariables()
        # Change all variables to True
        self.setVariablesTrue()
        # Print all variables
        self.printVariables()

    # Test check() and checkManual() methods
    def testCheckMethods(self):
        for systems in self.all_systems:
            try:
                print(f"\n*** {systems.name} ***")
                print(f"check: {systems.check()}")
            except AttributeError:
                print(f"{systems.name} does not have check() method")
            try:
                print(f"checkManual: {systems.checkManual()}")
            except AttributeError:
                print(f"{systems.name} does not have checkManual()method")
            try:
                print(f"checkAlert: {systems.checkAlert()}")
            except AttributeError:
                print(f"{systems.name} does not have checkAlert() method")
            try:
                print(f"checkAlertManual: {systems.checkAlertManual()}")
            except AttributeError:
                print(f"{systems.name} does not have checkAlertManual() method")
