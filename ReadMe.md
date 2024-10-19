# Documentation Report for the Central Control Unit (CCC) Program

## Introduction

This report provides a detailed overview of the Central Control Unit (CCC) program, which is designed to simulate a control system managing various subsystems within an automated environment. The program is written in Python and utilizes object-oriented programming principles to model real-world systems. The CCC oversees several critical subsystems, including Feeding, Fish Health Monitoring, Environmental Control Monitoring, Water Filtering, and Lighting. This documentation aims to explain the structure, functionality, and interactions within the program, offering insights into how each component operates individually and collectively.

---

## Program Structure

The CCC program is organized into four main Python files:

1. **`variable.py`**: Defines the `Variable` class used to represent inputs and outputs within the subsystems.
2. **`systems.py`**: Contains classes for each subsystem, inheriting from a base system class.
3. **`ccc.py`**: Implements the `CCC` class, which manages the subsystems and the multiplexer logic.
4. **`main.py`**: Serves as the entry point of the program, providing a user interface for interaction.

---

## 1. `variable.py` - Variable Class

The `Variable` class encapsulates the concept of a system variable with a name and a boolean value. It provides methods to set and retrieve the value, and a string representation for debugging purposes.

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

- **Purpose**: To model input and output variables within subsystems.
- **Attributes**:
  - `name`: A string representing the variable's name.
  - `value`: A boolean representing the variable's state.
- **Methods**:
  - `set_value(value)`: Sets the variable's value.
  - `get_value()`: Retrieves the variable's value.

---

## 2. `systems.py` - Subsystem Classes

### BaseSystem Class

All subsystem classes inherit from the `BaseSystem` class, which initializes common attributes and methods.

```python
class BaseSystem:
    def __init__(self):
        self.name = self.__class__.__name__ + " System"
        self.manual_switch = Variable("manual_switch", True)
        self.variables = []

    def getVariables(self):
        return self.variables
```

- **Purpose**: To provide common functionality and attributes to all subsystems.
- **Attributes**:
  - `name`: A string indicating the system's name.
  - `manual_switch`: A `Variable` object representing the manual override switch.
  - `variables`: A list to store all variables associated with the subsystem.

---

### Subsystem Implementations

Each subsystem is modeled as a class that extends `BaseSystem`, with specific variables and methods tailored to its functionality.

#### 2.1 Feeding System

Manages the automatic feeding process.

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
        output = (self.timer.get_value() and
                  self.water_quality.get_value() and
                  self.food_level.get_value())
        return self.manual_switch.get_value() or output if manual else output

    def checkAlert(self, manual=False):
        output = not self.food_level.get_value()
        return self.manual_switch.get_value() or output if manual else output
```

- **Variables**:
  - `timer`: Indicates if it's time to feed.
  - `water_quality`: Represents the quality of water.
  - `food_level`: Checks if there's sufficient food.
- **Methods**:
  - `check(manual=False)`: Determines if feeding should occur.
  - `checkAlert(manual=False)`: Checks for low food levels to trigger an alert.

#### 2.2 Fish Health Monitoring System

Monitors fish health through various sensors.

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
        output = not (self.feeding_response.get_value() and
                      self.fish_activity_level.get_value() and
                      self.bio_sensors.get_value() and
                      self.fish_behavioural_patterns.get_value())
        return self.manual_switch.get_value() or output if manual else output
```

- **Variables**:
  - `feeding_response`, `fish_activity_level`, `bio_sensors`, `fish_behavioural_patterns`: Various health indicators.
- **Methods**:
  - `checkAlert(manual=False)`: Determines if a health alert should be raised.

#### 2.3 Environmental Control Monitoring System

Ensures optimal environmental conditions.

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
        output = (self.pH.get_value() or
                  self.dissolved_oxygen.get_value() or
                  self.temperature.get_value())
        return self.manual_switch.get_value() or output if manual else output
```

- **Variables**:
  - `pH`, `dissolved_oxygen`, `temperature`: Environmental parameters.
- **Methods**:
  - `checkAlert(manual=False)`: Checks for environmental anomalies.

#### 2.4 Water Filtering System

Controls the filtration process.

```python
class WaterFiltering(BaseSystem):
    def __init__(self):
        super().__init__()
        self.turbidity = Variable("turbidity", False)
        self.pressure = Variable("pressure", False)
        self.variables.extend([self.turbidity, self.pressure, self.manual_switch])

    def check(self, manual=False):
        output = self.turbidity.get_value() and not self.pressure.get_value()
        return self.manual_switch.get_value() or output if manual else output
```

- **Variables**:
  - `turbidity`: Indicates water clarity.
  - `pressure`: Monitors pressure levels.
- **Methods**:
  - `check(manual=False)`: Determines if filtering is necessary.

#### 2.5 Lighting System

Manages lighting conditions.

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
        return self.manual_switch.get_value() or output if manual else output
```

- **Variables**:
  - `timer`: Controls scheduled lighting.
  - `ambient_light_level`: Measures external light levels.
- **Methods**:
  - `check(manual=False)`: Determines if lights should be turned on.

---

## 3. `ccc.py` - Central Control Unit Class

The `CCC` class orchestrates the interaction between subsystems and handles the multiplexer logic.

### Initialization

```python
class CCC:
    def __init__(self):
        self.feeding = Feeding()
        self.fish_health_monitoring = FishHealthMonitoring()
        self.environment_control_monitoring = EnvironmentalControlMonitoring()
        self.waterfiltering = WaterFiltering()
        self.lighting = Lighting()
        self.all_systems = [
            self.feeding, self.fish_health_monitoring,
            self.environment_control_monitoring, self.waterfiltering, self.lighting
        ]
```

- **Purpose**: To initialize subsystem instances and maintain a collective list.
- **Attributes**:
  - Individual subsystem instances.
  - `all_systems`: A list containing all subsystems for easy management.

### Multiplexer Methods

The multiplexer selects outputs from different subsystems based on selection bits.

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
        self.feeding.check(),
        self.feeding.checkAlert(),
        self.fish_health_monitoring.checkAlert(),
        self.environment_control_monitoring.checkAlert(),
        self.waterfiltering.check(),
        self.lighting.check(),
    ]
    return system_outputs[muxInput]
```

- **Selection Bits**:
  - `s1`: Most significant bit.
  - `s2`: Middle bit.
  - `s3`: Least significant bit.
- **Logic**:
  - Calculates `muxInput` to select the appropriate system output.
  - The `runMuxManual` method operates similarly but includes the `manual_switch`.

### Management Methods

- **`setManualSwitch(index)`**: Toggles the manual switch of a subsystem.
- **`printManualSwitches()`**: Displays the status of all manual switches.
- **`printVariables()`**: Lists all variables and their current values.
- **`setVariablesTrue()` / `setVariablesFalse()`**: Sets all subsystem variables (excluding `manual_switch`) to `True` or `False`.
- **`randomiseVariables()`**: Randomly assigns `True` or `False` to subsystem variables (excluding `manual_switch`).

---

## 4. `main.py` - Program Entry Point

The `main.py` script provides a command-line interface for user interaction, allowing users to control the CCC and its subsystems.

### User Interface Functions

- **`printBanner()`**: Displays the main menu.
- **`printSystems()`**: Lists all available subsystems.
- **`clear_screen()`**: Clears the console for a better user experience.
- **`mux_menu(manual=True)`**: Handles multiplexer interactions, prompting the user for selection bits and displaying outputs.

### Main Program Loop

```python
while True:
    clear_screen()
    printBanner()
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            # Toggle manual switch
        elif choice == 2:
            # Run Multiplexer
        elif choice == 3:
            # Set system variables
        elif choice == 4:
            break  # Exit the program
        else:
            print("Invalid choice!")
    except Exception as e:
        print("Error:", e)
```

- **Options**:
  1. **Toggle Manual Switch**: Allows toggling of manual overrides for subsystems.
  2. **Run Multiplexer (Mux)**: Enables users to input selection bits and observe system outputs.
  3. **Set System Variables**: Provides options to view, set, or randomize variables.
  4. **Exit**: Terminates the program.

---

## How to Use the Program

1. **Running the Program**:
   - Execute `main.py` using Python: `python main.py`.
2. **Navigating the Menu**:
   - Use numerical inputs to select options from the main menu.
3. **Toggling Manual Switches**:
   - Select option `1` and choose the subsystem by its index.
4. **Running the Multiplexer**:
   - Choose option `2`, decide whether to include the manual switch, and input the selection bits (`s1`, `s2`, `s3`).
5. **Setting System Variables**:
   - Select option `3` to view or modify subsystem variables.

---

## Example Scenario

1. **Initialize Variables**:
   - Start the program and set all variables to `True` using the system variables menu.
2. **Test Feeding System Output**:
   - Run the multiplexer without the manual switch.
   - Input selection bits `s1=0`, `s2=0`, `s3=0` to select the Feeding System output.
   - Observe the output, which should be `True`.
3. **Toggle Manual Switch**:
   - Toggle the manual switch for the Feeding System.
   - Run the multiplexer with the manual switch included.
   - Input the same selection bits and observe that the output remains `True` due to the manual override.
4. **Randomize Variables**:
   - Use the system variables menu to randomize variables.
   - Run the multiplexer again to see how outputs change based on different variable states.

---

## Conclusion

The Central Control Unit (CCC) program effectively simulates the control logic of an automated system with multiple subsystems. By leveraging object-oriented programming and a clear structural design, the program allows users to interact with and manipulate system variables, observe the impact of manual overrides, and understand the role of multiplexers in selecting system outputs. This documentation provides a comprehensive guide to the program's components and usage, enabling users to engage with the system confidently.

---

## Acknowledgments

This Markdown file was generated by ChatGPT. The Python code snippets were adapted from the original program files and formatted for documentation purposes.
This program demonstrates the integration of various programming concepts, including class inheritance, encapsulation, and bitwise operations, to model a complex control system. It serves as an educational tool for understanding system interactions and control mechanisms in automation.
