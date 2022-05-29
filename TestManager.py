from SimulatedLOXValve import SimulatedLOXValve
from LOXValveConnection import LOXValveConnection
class TestManager:
    def __init__(self, startingPressureDiff, endingPressureDiff):
        self.startingPressureDiff = startingPressureDiff
        self.endingPressureDiff = endingPressureDiff
        self.pressureDiff = startingPressureDiff
        self.simValve = SimulatedLOXValve()
        self.connection = LOXValveConnection()

    def runTest(self):
        while self.pressureDiff < self.endingPressureDiff:
            predictedFlowRate = self.simValve.calculateFlowRate(self.pressureDiff)
            realFlowRate = self.connection.measureFlowRate()
            self.pressureDiff += 0.2