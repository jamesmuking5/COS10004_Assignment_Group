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
        # List of all systems
        self.all_systems = [
            self.feeding,
            self.fish_health_monitoring,
            self.environment_control_monitoring,
            self.waterfiltering,
            self.lighting,
        ]
        # List of system outputs (Mux)
        self.system_outputs = [
            self.feeding.check(),  # d0
            self.feeding.checkAlert(),  # d1
            self.fish_health_monitoring.checkAlert(),  # d2
            self.environment_control_monitoring.checkAlert(),  # d3
            self.waterfiltering.check(),  # d4
            self.lighting.check(),  # d5
        ]
        # List of system outputs (Mux) for manual switch
        self.system_outputs_manual = [
            self.feeding.check(manual=True),  # d0
            self.feeding.checkAlert(manual=True),  # d1
            self.fish_health_monitoring.checkAlert(manual=True),  # d2
            self.environment_control_monitoring.checkAlert(manual=True),  # d3
            self.waterfiltering.check(manual=True),  # d4
            self.lighting.check(manual=True),  # d5
        ]

    # Mux selection and return output
    def runMux(self, s1, s2, s3):
        # If s1, s2, s3 are not 0 or 1, raise an error
        if s1 not in [0, 1] or s2 not in [0, 1] or s3 not in [0, 1]:
            raise ValueError("s1, s2, s3 must be 0 or 1")
        input = (s1 << 2) | (s2 << 1) | s3
        if input >= 6:
            raise IndexError("D0 - D5 only")
        return self.system_outputs[input]

    # Mux selection and return output for manual switch
    def runMuxManual(self, s1, s2, s3):
        # If s1, s2, s3 are not 0 or 1, raise an error
        if s1 not in [0, 1] or s2 not in [0, 1] or s3 not in [0, 1]:
            raise ValueError("s1, s2, s3 must be 0 or 1")
        input = (s1 << 2) | (s2 << 1) | s3
        if input >= 6:
            raise IndexError("D0 - D5 only")
        return self.system_outputs_manual[input]

    # Toggle manual_switch for chosen system
    def setManualSwitch(self, index):
        """
        Toggle manual_switch for chosen system. Choose system via integer index.

        Args:
            index (int): 1 - Feeding, 2 - Fish Health Monitoring, 3 - Environmental Control Monitoring, 4 - Water Filtering, 5 - Lighting
        """
        index -= 1
        if index < 0 or index >= len(self.all_systems):
            raise ValueError("Only 1 - 5 systems available")
        self.all_systems[index].manual_switch.set_value(
            not self.all_systems[index].manual_switch.get_value()
        )  # Toggle manual_switch

    def printManualSwitches(self):
        print("Manual Switches Status:")
        for system in self.all_systems:
            print(f"{system.name.ljust(40)} = {system.manual_switch.get_value()}")

    # Print all variables state
    def printVariables(self):
        for system in self.all_systems:
            print(f"\n*** {system.name} ***")
            for var in system.getVariables():
                print(f"{var.name.ljust(25)} = {var.value}")

    # Set all variables to True except manual_switch
    def setVariablesTrue(self):
        for system in self.all_systems:
            for var in system.getVariables():
                if var.name != "manual_switch":
                    var.set_value(True)

    # Set all variables to False except manual_switch
    def setVariablesFalse(self):
        for system in self.all_systems:
            for var in system.getVariables():
                if var.name != "manual_switch":
                    var.set_value(False)

    # Randomise all variables except manual_switch
    def randomiseVariables(self):
        for system in self.all_systems:
            for var in system.getVariables():
                if var.name != "manual_switch":
                    var.set_value(random.choice([True, False]))
