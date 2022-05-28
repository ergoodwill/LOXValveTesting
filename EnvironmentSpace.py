from EnvironmentNode import EnvironmentNode

class EnvironmentSpace:
    def __init__(self, startingPressure):
        self.startingNode = EnvironmentNode(startingPressure, parent=None)
        self.tree = EnvironmentNode

    def addNode(self, node):
        self.startingNode.addChild(node)

    def printTree(self):
        self.printTreeTraversal(self.startingNode)

    def printTreeTraversal(self, node):
        if node.left != None:
            self.printTreeTraversal(node.left)
        elif node.right != None:
            self.printTreeTraversal(node.right)
        print("Pressure:", node.pressure)