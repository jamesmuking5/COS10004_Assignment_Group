class Variable:

    # Constructor
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __repr__(self):
        return f"{self.name} ={self.value}"
