from variable import Variable


# Superclass
class BaseSystem:
    def __init__(self):
        self.name = self.__class__.__name__ + " System"
        self.manual_switch = Variable("manual_switch", False)
        self.variables = []

    def getVariables(self):
        return self.variables


# 2.1 Feeding (D0 - D1)
class Feeding(BaseSystem):
    def __init__(self):
        super().__init__()
        self.timer = Variable("timer", False)
        self.water_quality = Variable("water_quality", False)
        self.food_level = Variable("food_level", False)
        self.variables.extend(
            [self.timer, self.water_quality, self.food_level, self.manual_switch]
        )

    # check = output
    def check(self):
        """
        Feeding System\n
        O = TWF\n
        Checks if the feeder is activated.
        Returns:
            bool: True if the feeder is activated, False otherwise.
        """
        return (
            self.timer.get_value()
            and self.water_quality.get_value()
            and self.food_level.get_value()
        )

    def checkAlert(self):
        """
        O = F'\n
        Checks if the alert is activated.

        Returns:
            bool: True if the alert is activated, False otherwise.
        """
        return not self.food_level.get_value()

    def checkManual(self):
        """
        O = S + (TWF)\n
        Checks if the feeder is activated manually.

        Returns:
            bool: True if the feeder is activated manually, False otherwise.
        """
        return self.manual_switch.get_value() or self.check()

    def checkAlertManual(self):
        """
        O = S + F'\n
        Checks if the alert is activated manually.

        Returns:
            bool: True if the alert is activated manually, False otherwise.
        """
        return self.manual_switch.get_value() or self.checkAlert()


# 2.2 Fish Health Monitoring (D2)
class FishHealthMonitoring(BaseSystem):
    def __init__(self):
        super().__init__()
        self.feeding_response = Variable("feeding_response", False)
        self.fish_activity_level = Variable("fish_activity_level", False)
        self.bio_sensors = Variable("bio_sensors", False)
        self.fish_behavioural_patterns = Variable("fish_behavioural_patterns", False)
        self.variables.extend(
            [
                self.feeding_response,
                self.fish_activity_level,
                self.bio_sensors,
                self.fish_behavioural_patterns,
                self.manual_switch,
            ]
        )

    def checkAlert(self):
        """
        Fish Health Monitoring System\n
        O = A'+B'+C'+D'\n
        Checks if the health alert is activated.

        Returns:
            bool: True if the health alert is activated, False otherwise.
        """
        return not (
            self.feeding_response.get_value()
            and self.fish_activity_level.get_value()
            and self.bio_sensors.get_value()
            and self.fish_behavioural_patterns.get_value()
        )

    def checkAlertManual(self):
        """
        O = S + (A'+B'+C'+D')\n
        Checks if the health alert is activated manually.

        Returns:
            bool: True if the health alert is activated manually, False otherwise.
        """
        return self.manual_switch.get_value() or self.checkAlert()


# 2.3 Environmental Control Monitoring (D3)
class EnvironmentalControlMonitoring(BaseSystem):
    def __init__(self):
        super().__init__()
        self.pH = Variable("pH", False)
        self.dissolved_oxygen = Variable("dissolved_oxygen", False)
        self.temperature = Variable("temperature", False)
        self.variables.extend(
            [self.pH, self.dissolved_oxygen, self.temperature, self.manual_switch]
        )

    def checkAlert(self):
        """
        Environmental Control Monitoring System\n
        O = P + D + T\n
        Checks if the alert is activated.

        Returns:
            bool: True if the alert is activated, False otherwise.
        """
        return (
            self.pH.get_value()
            or self.dissolved_oxygen.get_value()
            or self.temperature.get_value()
        )

    def checkAlertManual(self):
        """
        O = S + (P + D + T)\n
        Checks if the alert is activated manually.

        Returns:
            bool: True if the alert is activated manually, False otherwise.
        """
        return self.manual_switch.get_value() or self.checkAlert()


# 2.4 Water Filtering (D4)
class WaterFiltering(BaseSystem):
    def __init__(self):
        super().__init__()
        self.turbidity = Variable("turbidity", False)
        self.pressure = Variable("pressure", False)
        self.variables.extend([self.turbidity, self.pressure, self.manual_switch])

    def check(self):
        """
        Water Filtering System\n
        O = TP'\n
        Checks if the filter is activated.

        Returns:
            bool: True if the filter is activated, False otherwise.
        """
        return self.turbidity.get_value() and not self.pressure.get_value()

    def checkManual(self):
        """
        O = S + (TP')\n
        Checks if the filter pump is activated manually.

        Returns:
            bool: True if the filter pump is activated manually, False otherwise.
        """
        return self.manual_switch.get_value() or self.check()


# 2.5 Lighting (D5)
class Lighting(BaseSystem):
    def __init__(self):
        super().__init__()
        self.timer = Variable("timer", False)
        self.ambient_light_level = Variable("ambient_light_level", False)
        self.variables.extend(
            [self.timer, self.ambient_light_level, self.manual_switch]
        )

    def check(self):
        """
        Lighting System\n
        O = T + A'\n
        Checks if the light is activated.

        Returns:
            bool: True if the light is activated, False otherwise.
        """
        return self.timer.get_value() or not self.ambient_light_level.get_value()

    def checkManual(self):
        """
        O = S + (T + A')\n
        Checks if the light is activated manually.

        Returns:
            bool: True if the light is activated manually, False otherwise.
        """
        return self.manual_switch.get_value() or self.check()


# Free (D6-D7)
