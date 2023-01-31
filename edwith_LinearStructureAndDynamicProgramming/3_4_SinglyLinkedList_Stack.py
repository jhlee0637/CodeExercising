'''
Stacks are the name of data structure.
Stacks are linear like linked lists.
You can only access to the end of stack.
You can't insert or delete the data from middle. (Last In First Out)

Stack has two operations.
1) Push: insert an instance at the first in the linked list.
2) Pop: remove and return an instance at the first in the linked list.
'''
from ImportOnly.SinglyLinkedList import SinglyLinkedList

class Stack(object):
    lstInstance = SinglyLinkedList()

    def pop(self):
        return self.lstInstance.removeAt(0) #remove from first

    def push(self, value):
        self.lstInstance.insertAt(value, 0) #insert to first

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")

print(stack.pop()) #c
print(stack.pop()) #b
print(stack.pop()) #a