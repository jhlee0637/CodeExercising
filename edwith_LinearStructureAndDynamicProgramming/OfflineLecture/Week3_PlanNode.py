class PlanNode:
    def __init__(self, numNo, strSerialNumber, strModel, numModelNumber, dateStart, numAssemblyOrder, dateEnd,
                 strOrderOrigin):
        self.numNo = numNo
        self.strSerialNumber = strSerialNumber
        self.strModel = strModel
        self.numModelNumber = numModelNumber
        self.dateStart = dateStart
        self.numAssemblyOrder = numAssemblyOrder
        self.dateEnd = dateEnd
        self.strOrderOrigin = strOrderOrigin

    def printOut(self):
        print('No :', self.numNo, ', SerialNum : ', self.strSerialNumber, ',Model:', self.strModel, ',Start Date:',
              self.dateStart)

    def getNextNode(self):
        # Problem 1. complete this method
        NextNode = self.NextNode 
        return NextNode

    def getPrevNode(self):
        # Problem 1. complete this method
        PrevNode = self.PrevNode
        return PrevNode

    def setNextNode(self, node):
        # Problem 1. complete this method
        self.NextNode = node

    def setPrevNode(self, node):
        # Problem 1. complete this method
        self.PrevNode = node