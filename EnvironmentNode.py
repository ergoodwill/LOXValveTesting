class EnvironmentNode:
    def __init__(self, pressure, parent):
        self.pressure = pressure
        self.left = None
        self.right = None
        self.parent = parent

    def addChild(self, child):
        if (child.pressure >= self.pressure):
            if self.left is None:
                self.left = child
            else:
                self.left.addChild(child)
        elif self.right is None:
            self.right = child
        else:
            self.right.addChild(child)

    def setParent(self, parent):
        self.parent = parent

    def setPressure(self, pressure):
        self.pressure = pressure