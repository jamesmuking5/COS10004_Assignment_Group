from variable import Variable
from systems import (
    Feeding,
    FishHealthMonitoring,
    EnvironmentalControlMonitoring,
    WaterFiltering,
    Lighting,
)

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

    def testSystems(self):
        # Print all variables
        for system in self.all_systems:
            print(f"\n*** {system.name} ***")
            for var in system.getVariables():
                print(var)
        # Change all variables to True
        print("\n**************** Changing all variables to True ********************")
        for system in self.all_systems:
            for var in system.getVariables():
                var.set_value(True)
        # Print all variables
        for system in self.all_systems:
            print(f"\n*** {system.name} ***")
            for var in system.getVariables():
                print(var)

    # Test systems
    def feedingTest(self):
        for var in self.feeding.getVariables():
            print(var)

    def testrun(self):
        # Test run
        print("Feeding System")
        print("Feeder activated:", self.feeding.checkFeeder())
        print("Alert activated:", self.feeding.checkAlert())
        print("Feeder activated manually:", self.feeding.checkFeederManual())
        print("Alert activated manually:", self.feeding.checkAlertManual())

        # print("\nFish Health Monitoring System")
        # print("Feeding response:", self.fish_health_monitoring.checkFeedingResponse())
        # print(
        #     "Water quality response:",
        #     self.fish_health_monitoring.checkWaterQualityResponse(),
        # )
        # print(
        #     "Environment control response:",
        #     self.fish_health_monitoring.checkEnvironmentControlResponse(),
        # )

        # print("\nEnvironmental Control Monitoring System")
        # print(
        #     "Lighting response:",
        #     self.environment_control_monitoring.checkLightingResponse(),
        # )
        # print(
        #     "Water quality response:",
        #     self.environment_control_monitoring.checkWaterQualityResponse(),
        # )

        # print("\nWater Filtering System")
        # print("Water quality:", self.waterfiltering.checkWaterQuality())
        # print(
        #     "Water filter activated manually:",
        #     self.waterfiltering.checkWaterFilterManual(),
        # )

        # print("\nLighting System")
        # print("Lighting timer:", self.lighting.checkLightingTimer())
        # print("Lighting activated manually:", self.lighting.checkLightingManual())
