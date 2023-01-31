'''
Queues are the name of data structure.
Queues are linear like linked lists.
You can insert to the first of queue.
You can remove from the end of queue.
You can't insert or delete the data from middle. (First In First Out)

Queue has two operations.
1) Enqueue: insert an instance at the last in the linked list.
2) Dequeue: remove and return an instance at the first in the linked list.
'''
from ImportOnly.SinglyLinkedList import SinglyLinkedList

class Queue(object):
    lstInstance = SinglyLinkedList()

    def dequeue(self):
        return self.lstInstance.removeAt(0) #remove from first

    def enqueue(self, value):
        self.lstInstance.insertAt(value, self.lstInstance.getSize()) #insert to end

queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")

print (queue.dequeue()) #a
print (queue.dequeue()) #b
print (queue.dequeue()) #c