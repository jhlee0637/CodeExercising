'''
This is a copy of '6_1_TreeStructure_TreeNode.py'
'''
class TreeNode:
    nodeLHS = None #next node1: Left hand side - when values have "lower" than it's own value
    nodeRHS = None #next node2: Right hand side - when values have "higher" than it's own value
    nodeParent = None #previous node
    value = None

    def __init__(self, value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent

    def getLHS(self):
        return self.nodeLHS
    def getRHS(self):
        return self.nodeRHS
    def getValue(self):
        return self.value
    def getParent(self):
        return self.nodeParent

    def setLHS(self, LHS):
        self.nodeLHS = LHS
    def setRHS(self, RHS):
        self.nodeRHS = RHS
    def setValue(self, value):
        self.value = value
    def setParent(self, nodeParent):
        self.nodeParent = nodeParent