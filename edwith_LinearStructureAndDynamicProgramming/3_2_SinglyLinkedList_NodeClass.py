'''
Singly linked list: a type of data structure.
                    It's built with several nodes.
                    Each nodes are linked with their own reference values. (except head and tail nodes)

Before we implement a singly linked list,
we should define the Node class.
'''
class Node:
    nodeNext = None
    nodePrev = ''
    objValue = ''
    blnHead = False #head and tail nodes are optional.
    blnTail = False #having head and tail makes implementation very convenient.
    
    def __init__(self, objValue='', nodeNext = None, blnHead = False, blnTail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.blnHead = blnHead
        self.blnTail =blnTail
    
    def getValue(self): #node has a variable to it's reference value
        return self.objValue
    def setValue(self, objValue):
        self.objValue = objValue

    def getNext(self): #node has a variable to it's next node
        return self.nodeNext
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext

    def isHead(self):
        return self.blnHead
    def isTail(self):
        return self.blnTail

node1 = Node(objValue = 'a')
nodeTail = Node(blnTail = True)
nodeHead = Node(blnHead = True, nodeNext = node1)