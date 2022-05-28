from EnvironmentNode import EnvironmentNode

class EnvironmentSpace:
    def __init__(self, startingPressure):
        self.startingNode = EnvironmentNode(startingPressure, parent=None)
        self.tree = EnvironmentNode

    def addNode(self, node):
        self.startingNode.addChild(node)

    def printTree(self):
        self.printTree(self.startingNode)

    def printTree(self, node):
        if node.left != None:
            self.printTree(node.left)
        elif node.right != None:
            self.printTree(node.right)
        print("Pressure:", node.pressure)