from node import Node

class queue_class:

    def __init__(self):
        self._front = None
        self._back = None

    def enqueue(self, entry):
        if self.is_empty():
            self._front = Node(entry)
            self._back = self._front
        else:
            new_back = Node(entry)
            self._back.next = new_back
            self._back = new_back

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('Queue is Empty')
        elif self._front == self._back:
            temp = self._front.entry
            self._front = None
            self._back = None
            return temp
        else:
            temp = self._front.entry
            self._front = self._front.next
            return temp

    def peek_front(self):
        if self._front != None:
            return self._front.entry
        else:
            raise RuntimeError('Queue is empty')

    def is_empty(self):
        if self._front == None:
            return True
        else:
            return False