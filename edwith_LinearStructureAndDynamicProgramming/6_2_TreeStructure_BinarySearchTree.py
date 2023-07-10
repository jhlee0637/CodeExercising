'''
Binary Search Tree(BST) is one of the simplest tree structure.
Each node from BST is built within two next nodes, as like the tree node we just built from '6_1_TreeStructure_TreeNode.py'

Let's implement BST with the several operations(insert, delete, search, travse, ...)
'''
from ImportOnly.TreeNode import TreeNode

class BinarySearchTree:
    root = None

    def __init__(self):
        pass

    def insert(self, value, node = None):
        if node is None:
            node = self.root
        #Before insertion, the operation to look for a place to insert is run by recursions. -> so we write down 'escape route' from the recursions on here.
        if self.root is None:
            self.root = TreeNode(value, None) #if there is no root, you are the root now
            return
        if value == node.getValue(): #if the value is equal to the vaule to insert
            return #return already there
        #try to insert to RHS
        if value > node.getValue(): #if the value is smaller than the value to insert, try to insert to RHS
            if node.getRHS() is None:
                node.setRHS(TreeNode(value, node)) #insert to RHS
            else:
                self.insert(value, node.getRHS()) #if RHS is not empty, recursion(go down to the next level of that RHS)
        #try to insert to LHS
        if value < node.getValue():
            if node.getLHS() is None:
                node.setLHS(TreeNode(value, node))
            else:
                self.insert(value, node.hetHLS)

    def search(self, value, node = None):
        #initiating from a root
        if node is None: 
            node = self.root
        #Searching uses recursion too -> we need 'escape' in here too.
        if value == node.getValue():
            return True
        #search from the RHS
        if value > node.getValue(): #if the value is smaller than the value to search, look at the RHS
            if node.getRHS() is None:
                return False #if there is no node in RHS, FALSE
            else:
                return self.search(value, node.getRHS()) #if there is node, recursion
        #search from the LHS
        if value < node.getValue():
            if node.getLHS() is None:
                return False
            else:
                return self.search(value, node.getLHS()) #recursion
        
    def delete(self, value, node = None):
        #initiating from a root
        if node is None:
            node = self.root
        #find a node to delete through recursions
        if node.getValue() < value:
            return self.delete(value, node.getRHS())
        if node.getValue() > value:
            return self.delete(value, node.getLHS())
        #there are three cases to delete node from the BST
        if node.getValue() == value:
            if node.getLHS() is not None and node.getRHS() is not None: #case1) the node has both LHS and RHS -> we can choose one of them to replace the deleted node. -> Let's choose RHS -> the minium value from RHS's childs will replace the current value.
                nodeMin = self.findMin(node.getRHS) #function 'findMin' will be defined later.
                node.setValue(nodeMin.getValue())
                self.delete(nodeMin.getValue(), node.getRHS())
                return
            parent = node.getParent()
            if node.getLHS() is not None: #case2) the node has one child(LHS)
                if node == self.root:
                    self.root = node.getLHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else:
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return
            if node.getRHS() is not None: #case2) the node has one child(RHS)
                if node == self.root:
                    self.root = node.getRHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getRHS())
                    node.getRHS().setParent(parent)
                else:
                    parent.setRHS(node.getRHS())
                    node.getRHS().setParent(parent)
                return
            if node == self.root: #case3) if there are no childs
                self.root = None
            elif parent.getLHS() == node:
                parent.setLHS(None)
            else:
                parent.setRHS(None)
            return

    def findMax(self, node = None): #the end of RHS is the maximum - keep recursion
        if node is None:
            node - self.root
        if node.getRHS() is None:
            return node
        return self.findMax(node.getRHS())

    def findMin(self, node = None): #the end of LHS is the minimum - keep recursion
        if node is None:
            node = self.root
        if node.getLHS() is None:
            return node
        return self.findMin(node.getLHS())

    def traverseLevelOrder(self):
        pass
    def traverseInOrder(self, node = None):
        pass
    def traversePreOrder(self, node = None):
        pass
    def traversePostOrder(self, node = None):
        pass
