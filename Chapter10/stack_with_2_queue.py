from fix_size_queue import FixSizeQueue

class Stack:
    def __init__(self, size=100):
        self.queue1 = FixSizeQueue(size)
        self.queue2 = FixSizeQueue(size)
        self.queueToEnqueue = self.queue1
        self.queueEmpty = self.queue2

    def push(self, x):
        self.queueToEnqueue.enqueue(x)

    def pop(self):
        lastIterVal = None
        thisIterVal = None
        try:
            while True:
                thisIterVal = self.queueToEnqueue.dequeue()
                if lastIterVal is not None:
                    self.queueEmpty.enqueue(lastIterVal)
                thisIterVal, lastIterVal = None, thisIterVal
        except Exception:
            self.queueToEnqueue, self.queueEmpty = self.queueEmpty, self.queueToEnqueue

        return lastIterVal

