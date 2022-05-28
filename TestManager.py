from EnvironmentSpace import EnvironmentSpace

class TestManager:
    def __init__(self, startingPressure):
        self.startingPressure = startingPressure
        self.environmentSpace = EnvironmentSpace(startingPressure)

    def showEnvironmentSpace(self):
        self.environmentSpace.printTree()