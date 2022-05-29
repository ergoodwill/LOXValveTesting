import Constants
import numpy as np

class SimulatedLOXValve:
    def __init__(self):
        self.findFlowCoefficient()

    def findFlowCoefficient(self):
        self.flowCoefficient = Constants.F1_FLOWRATE * np.sqrt(Constants.LOX_SG/Constants.F1_PRESSDROP)

    def calculateFlowRate(self, pressureDiff):
        flowRate = self.flowCoefficient*np.sqrt(pressureDiff/Constants.LOX_SG)
        return flowRate