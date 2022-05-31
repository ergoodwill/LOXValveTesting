import numpy as np
from SimulatedLOXValve import SimulatedLOXValve
from LOXValveConnection import LOXValveConnection
from Plotter import Plotter

class TestManager:
    def __init__(self, startingPressureDiff, endingPressureDiff, startingPressure, endingPressure):
        self.startingPressureDiff = startingPressureDiff
        self.endingPressureDiff = endingPressureDiff
        self.pressureDiff = startingPressureDiff

        self.startingPressure = startingPressure
        self.endingPressure = endingPressure
        self.pressure = startingPressure

        self.simValve = SimulatedLOXValve()
        self.connection = LOXValveConnection()
        self.connection.establishConnection()

        self.plotter = Plotter()

    def runTest(self):
        while (self.pressure < self.endingPressure):
            while self.pressureDiff < self.endingPressureDiff:
                predictedFlowRate = self.simValve.calculateFlowRate(self.pressureDiff)
                realFlowRate = self.connection.measureFlowRate(self.pressureDiff, self.pressure)
                self.plotter.addToData(self.pressureDiff, self.pressure, np.absolute(predictedFlowRate-realFlowRate))
                self.pressureDiff += 0.2
            self.pressure += 10
            self.pressureDiff = self.startingPressureDiff
        self.plotter.plot()