import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plotter:
    def __init__(self):
        self.pressureDiffList =[]
        self.pressureList = []
        self.errorList = []

    def addToData(self, pressureDiff, pressure, error):
        self.pressureDiffList.append(pressureDiff)
        self.pressureList.append(pressure)
        self.errorList.append(error)

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot3D(self.pressureDiffList, self.pressureList, self.errorList)
        plt.show()