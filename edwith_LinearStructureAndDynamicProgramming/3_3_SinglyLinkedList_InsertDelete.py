'''
Implement singly linked list using the node class we definied.
We can do insertion or deletion of nodes from singly link list.

1) Insert procedure: store the new node
                     update the previous node to point the new node
                     update the new node to point the next node

2) Delete procedure: retrieve the next node
                     update the previous node to point the next node
'''
from ImportOnly.NodeClass import Node 

class SinglyLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0
    def __init__(self):
        self.nodeTail = Node(blnTail=True)
        self.nodeHead = Node(blnHead=True, nodeNext = self.nodeTail)

    def insertAt(self, objInsert, idxInsert): 
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert - 1) #get the previous node through the method 'get' which is defined from below
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1

    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()

    def get(self, idxRetrieve): #method 'get' to get which index's node
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end=" ")
        print("")

    def getSize(self):
        return self.size

'''
Let's try:  a - b - d - e - f

            a - b -"c"- d - e - f

            a - b - c ----- e - f
'''
list1 = SinglyLinkedList()
list1.insertAt('a',0)
list1.insertAt('b',1)
list1.insertAt('d',2)
list1.insertAt('e',3)
list1.insertAt('f',4)
list1.printStatus()

list1.insertAt('c',2) #insert the node at the middle of the array
list1.printStatus()

list1.removeAt(3) #delete the node at the middle of the array 
list1.printStatus()