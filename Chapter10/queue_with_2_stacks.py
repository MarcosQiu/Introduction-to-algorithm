class Queue:
    def __init__(self):
        self.enqueueStack = list()
        self.dequeueStack = list()

    def enqueue(self, x):
        self.enqueueStack.append(x)

    def dequeue(self):
        if len(self.dequeueStack) == 0:
            while len(self.enqueueStack) > 0:
                self.dequeueStack.append(self.enqueueStack.pop())

        return self.dequeueStack.pop()