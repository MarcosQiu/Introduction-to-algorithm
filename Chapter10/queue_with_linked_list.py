from node import Node


class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def enqueue(self, x):
        self.tail.set_next(Node(x))
        self.tail = self.tail.get_next()

    def dequeue(self):
        assert self.head.get_next() is not None, 'Cannot dequeue from empty queue'

        el = self.head.get_next().get_val()
        self.head.set_next(self.head.get_next().get_next())
        # in case that all the elements are dequeued, tail
        # still points to some node that is already not part
        # of the queue
        if self.head.get_next() is None:
            self.tail = self.head
        return el


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    while True:
        try:
            print(q.dequeue())
        except AssertionError:
            break
