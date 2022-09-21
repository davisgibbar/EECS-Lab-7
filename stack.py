from node import Node

class stack_class:

    def __init__(self):
        self._top = None

    def push(self, entry):
        if self.is_empty():
            self._top = Node(entry)
        else:
            temp_node = self._top
            self._top = Node(entry)
            self._top.next = temp_node

    def pop(self):
        if self.is_empty():
            self._top = None
        else:
            temp = self._top.entry
            self._top = self._top.next
            return temp

    def peek(self):
        if self._top != None:
            return self._top.entry
        else:
            raise RuntimeError('Stack Empty')

    def is_empty(self):
        if self._top == None:
            return True
        else:
            return False