# Central Control Unit (CCC) Documentation

## Introduction

This documentation provides an overview and explanation of the Central Control Unit (CCC) program, which simulates a control system for managing various subsystems in an automated environment. The program is designed using object-oriented programming principles in Python and includes a command-line interface for user interaction.

The CCC manages the following subsystems:

- Feeding System
- Fish Health Monitoring System
- Environmental Control Monitoring System
- Water Filtering System
- Lighting System

Each subsystem has its own set of input variables and outputs, which are controlled and monitored by the CCC. The program also implements a multiplexer (Mux) to select outputs from different subsystems based on user input.

---

## Project Structure

The project consists of the following Python files:

1. `main.py`: The main script that runs the program and handles user interaction.
2. `systems.py`: Defines the subsystem classes and their functionalities.
3. `ccc.py`: Contains the `CCC` class that manages all subsystems and the multiplexer logic.
4. `variable.py`: Defines the `Variable` class used to represent input and output variables.

---

## Detailed Explanation

### 1. `variable.py`

#### `Variable` Class

The `Variable` class represents a variable with a name and a boolean value. It includes methods to set and get the variable's value.

```python
class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __repr__(self):
        return f"{self.name} = {self.value}"
```

---

### 2. `systems.py`

#### `BaseSystem` Class

The `BaseSystem` class serves as a superclass for all subsystem classes. It initializes the `manual_switch` variable and maintains a list of variables associated with each subsystem.

```python
class BaseSystem:
    def __init__(self):
        self.name = self.__class__.__name__ + " System"
        self.manual_switch = Variable("manual_switch", True)
        self.variables = []

    def getVariables(self):
        return self.variables
```

---

#### Subsystem Classes

Each subsystem class inherits from `BaseSystem` and implements specific functionality.

##### **a. Feeding System**

- **Purpose**: Manages the feeding mechanism.
- **Variables**:
  - `timer`
  - `water_quality`
  - `food_level`
  - `manual_switch` (inherited)
- **Methods**:
  - `check(manual=False)`: Determines if the feeder should be activated.
  - `checkAlert(manual=False)`: Checks if an alert should be activated due to low food levels.

```python
class Feeding(BaseSystem):
    def __init__(self):
        super().__init__()
        self.timer = Variable("timer", False)
        self.water_quality = Variable("water_quality", False)
        self.food_level = Variable("food_level", False)
        self.variables.extend([
            self.timer, self.water_quality, self.food_level, self.manual_switch
        ])

    def check(self, manual=False):
        output = (
            self.timer.get_value() and
            self.water_quality.get_value() and
            self.food_level.get_value()
        )
        if manual:
            return self.manual_switch.get_value() or output
        return output

    def checkAlert(self, manual=False):
        output = not self.food_level.get_value()
        if manual:
            return self.manual_switch.get_value() or output
        return output
```

---

##### **b. Fish Health Monitoring System**

- **Purpose**: Monitors the health of fish based on various sensors.
- **Variables**:
  - `feeding_response`
  - `fish_activity_level`
  - `bio_sensors`
  - `fish_behavioural_patterns`
  - `manual_switch` (inherited)
- **Methods**:
  - `checkAlert(manual=False)`: Determines if a health alert should be activated.

```python
class FishHealthMonitoring(BaseSystem):
    def __init__(self):
        super().__init__()
        self.feeding_response = Variable("feeding_response", False)
        self.fish_activity_level = Variable("fish_activity_level", False)
        self.bio_sensors = Variable("bio_sensors", False)
        self.fish_behavioural_patterns = Variable("fish_behavioural_patterns", False)
        self.variables.extend([
            self.feeding_response, self.fish_activity_level,
            self.bio_sensors, self.fish_behavioural_patterns, self.manual_switch
        ])

    def checkAlert(self, manual=False):
        output = not (
            self.feeding_response.get_value() and
            self.fish_activity_level.get_value() and
            self.bio_sensors.get_value() and
            self.fish_behavioural_patterns.get_value()
        )
        if manual:
            return self.manual_switch.get_value() or output
        return output
```

---

##### **c. Environmental Control Monitoring System**

- **Purpose**: Monitors environmental parameters like pH, dissolved oxygen, and temperature.
- **Variables**:
  - `pH`
  - `dissolved_oxygen`
  - `temperature`
  - `manual_switch` (inherited)
- **Methods**:
  - `checkAlert(manual=False)`: Determines if an environmental alert should be activated.

```python
class EnvironmentalControlMonitoring(BaseSystem):
    def __init__(self):
        super().__init__()
        self.pH = Variable("pH", False)
        self.dissolved_oxygen = Variable("dissolved_oxygen", False)
        self.temperature = Variable("temperature", False)
        self.variables.extend([
            self.pH, self.dissolved_oxygen, self.temperature, self.manual_switch
        ])

    def checkAlert(self, manual=False):
        output = (
            self.pH.get_value() or
            self.dissolved_oxygen.get_value() or
            self.temperature.get_value()
        )
        if manual:
            return self.manual_switch.get_value() or output
        return output
```

---

##### **d. Water Filtering System**

- **Purpose**: Manages the water filtering process based on turbidity and pressure.
- **Variables**:
  - `turbidity`
  - `pressure`
  - `manual_switch` (inherited)
- **Methods**:
  - `check(manual=False)`: Determines if the filter should be activated.

```python
class WaterFiltering(BaseSystem):
    def __init__(self):
        super().__init__()
        self.turbidity = Variable("turbidity", False)
        self.pressure = Variable("pressure", False)
        self.variables.extend([
            self.turbidity, self.pressure, self.manual_switch
        ])

    def check(self, manual=False):
        output = self.turbidity.get_value() and not self.pressure.get_value()
        if manual:
            return self.manual_switch.get_value() or output
        return output
```

---

##### **e. Lighting System**

- **Purpose**: Controls the lighting based on a timer and ambient light levels.
- **Variables**:
  - `timer`
  - `ambient_light_level`
  - `manual_switch` (inherited)
- **Methods**:
  - `check(manual=False)`: Determines if the lights should be activated.

```python
class Lighting(BaseSystem):
    def __init__(self):
        super().__init__()
        self.timer = Variable("timer", False)
        self.ambient_light_level = Variable("ambient_light_level", False)
        self.variables.extend([
            self.timer, self.ambient_light_level, self.manual_switch
        ])

    def check(self, manual=False):
        output = self.timer.get_value() or not self.ambient_light_level.get_value()
        if manual:
            return self.manual_switch.get_value() or output
        return output
```

---

### 3. `ccc.py`

#### `CCC` Class

The `CCC` (Central Control Unit) class manages all subsystems and the multiplexer logic.

##### **Initialization**

- Initializes all subsystem instances.
- Maintains a list of all subsystems.

```python
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
            self.feeding, self.fish_health_monitoring,
            self.environment_control_monitoring, self.waterfiltering, self.lighting
        ]
```

---

##### **Multiplexer Methods**

The multiplexer (Mux) selects one of the system outputs based on three selection bits (`s1`, `s2`, `s3`).

- **`runMux(s1, s2, s3)`:** Returns the output of the selected system without considering the manual switch.
- **`runMuxManual(s1, s2, s3)`:** Returns the output of the selected system considering the manual switch.

```python
def runMux(self, s1, s2, s3):
    # Validate input
    if s1 not in [0, 1] or s2 not in [0, 1] or s3 not in [0, 1]:
        raise ValueError("s1, s2, s3 must be 0 or 1")
    muxInput = (s1 << 2) | (s2 << 1) | s3
    if muxInput >= 6:
        raise IndexError("Only D0 to D5 are available")
    # Recompute system outputs
    system_outputs = [
        self.feeding.check(),                      # D0
        self.feeding.checkAlert(),                 # D1
        self.fish_health_monitoring.checkAlert(),  # D2
        self.environment_control_monitoring.checkAlert(),                                        # D3
        self.waterfiltering.check(),               # D4
        self.lighting.check(),                     # D5
    ]
    return system_outputs[muxInput]

def runMuxManual(self, s1, s2, s3):
    # Validate input
    if s1 not in [0, 1] or s2 not in [0, 1] or s3 not in [0, 1]:
        raise ValueError("s1, s2, s3 must be 0 or 1")
    muxInput = (s1 << 2) | (s2 << 1) | s3
    if muxInput >= 6:
        raise IndexError("Only D0 to D5 are available")
    # Recompute system outputs
    system_outputs = [
        self.feeding.check(manual=True),                      # D0
        self.feeding.checkAlert(manual=True),                 # D1
        self.fish_health_monitoring.checkAlert(manual=True),  # D2
        self.environment_control_monitoring.checkAlert(manual=True),                                        # D3
        self.waterfiltering.check(manual=True),               # D4
        self.lighting.check(manual=True),                     # D5
    ]
    return system_outputs[muxInput]
```

**Note**: The `muxInput` calculation maps the selection bits to the correct system outputs.

---

##### **Other Methods**

- **`setManualSwitch(index)`:** Toggles the `manual_switch` of the specified subsystem.
- **`printManualSwitches()`:** Displays the status of manual switches for all subsystems.
- **`printVariables()`:** Displays the current values of all variables in each subsystem.
- **`setVariablesTrue()`:** Sets all variables (except `manual_switch`) to `True`.
- **`setVariablesFalse()`:** Sets all variables (except `manual_switch`) to `False`.
- **`randomiseVariables()`:** Randomizes all variables (except `manual_switch`).

---

### 4. `main.py`

This is the main script that runs the program and provides a command-line interface for user interaction.

#### **Main Menu Options**

1. **Toggle Manual Switch**
   - Allows the user to toggle the `manual_switch` of a subsystem.
2. **Run Multiplexer (Mux)**
   - Prompts the user for selection bits (`s1`, `s2`, `s3`) and displays the output of the selected system.
   - The user can choose to include the `manual_switch` in the system's input.
3. **Set System Variables**
   - Provides options to view current variables, set all variables to `True` or `False`, or randomize variables.
4. **Exit**
   - Exits the program.

---

#### **Functions**

- **`printBanner()`:** Displays the main menu banner.
- **`printSystems()`:** Lists all subsystems.
- **`clear_screen()`:** Clears the console screen.
- **`mux_menu(manual=True)`:** Handles the multiplexer menu and user input for selection bits.

---

#### **Program Flow**

1. The program initializes the CCC instance.
2. Enters a main loop displaying the main menu.
3. Based on user input, it calls the appropriate functions.
4. Provides options to interact with subsystems and view or modify their states.
5. Allows running the multiplexer to see the outputs of different subsystems.

---

## How to Run the Program

1. **Ensure all files are in the same directory:**
   - `main.py`
   - `systems.py`
   - `ccc.py`
   - `variable.py`
2. **Run the main script:**

   ```bash
   python main.py
   ```

3. **Interact with the program via the command-line interface.**

---

## Example Usage

**1. Toggle Manual Switch**

- Choose option `1` from the main menu.
- Select a subsystem to toggle its `manual_switch`.

**2. Run Multiplexer (Mux)**

- Choose option `2` from the main menu.
- Decide whether to include the `manual_switch` in the system input.
- Input the selection bits (`s1`, `s2`, `s3`).
- View the output of the selected system.

**3. Set System Variables**

- Choose option `3` from the main menu.
- View current variables, set all to `True` or `False`, or randomize them.

---

## Example Scenario

1. **Start the Program**

   - Run `python main.py`.

2. **Set All Variables to True**

   - Choose option `3` (Set system variables).
   - Select option `2` (Set all variables to True).

3. **Run Mux Without Manual Switch**

   - Return to the main menu.
   - Choose option `2` (Run Multiplexer).
   - Select option `2` (No manual switch).
   - Input selection bits `s1=0`, `s2=0`, `s3=0` (Selecting D0).
   - The output should be `True` since all variables are set to `True`.

4. **Toggle Manual Switch for Feeding System**

   - Return to the main menu.
   - Choose option `1` (Toggle manual switch).
   - Select the Feeding System.
   - The manual switch for the Feeding System is now toggled.

5. **Run Mux With Manual Switch**
   - Return to the main menu.
   - Choose option `2` (Run Multiplexer).
   - Select option `1` (Include manual switch).
   - Input selection bits `s1=0`, `s2=0`, `s3=0` (Selecting D0).
   - The output should be `True` because the manual switch is active.

---

## Conclusion

This program provides a simulation of a central control system managing multiple subsystems with various inputs and outputs. By interacting with the command-line interface, users can monitor and control different aspects of the systems, test the multiplexer functionality, and observe how manual overrides affect system behavior.

---

**Note**: This documentation is generated by ChatGPT and is intended to guide users through understanding and using the CCC program effectively. For further assistance or questions, please refer to the code comments and docstrings within each Python file.
