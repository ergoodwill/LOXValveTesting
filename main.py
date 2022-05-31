from TestManager import TestManager

if __name__ == '__main__':
    TM = TestManager(startingPressureDiff=4.4, endingPressureDiff=8, startingPressure=50, endingPressure=450)
    TM.runTest()
