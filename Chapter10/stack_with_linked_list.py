from node import Node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        self.head = Node(x, self.head)

    def pop(self):
        assert self.head is not None, 'Cannot pop from empty stack.'
        el = self.head.get_val()
        self.head = self.head.get_next()
        return el
