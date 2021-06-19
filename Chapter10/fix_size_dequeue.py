class FixSizeDequeue:
    def __init__(size=10):
        self.size = size
        self.q = [None] * size
        self.tail = 1
        self.head = 0

    def enqueueHead(self, x):
        if self.head == self.tail:
            raise Exception('Queue overflow')

        self.q[self.head] = x
        self.head = (self.head + self.size - 1) % self.size
    
    def enqueueTail(self, x):
        if self.head == self.tail:
            raise Exception('Queue overflow')

        self.q[self.tail] = x
        self.tail = (self.tail + 1) % self.size

    def dequeueHead(self):
        if (self.head + 1) % self.size == self.tail:
            raise Exception('Queue underflow')

        x = self.q[self.head]
        self.head = (self.head + 1) % self.size

        return x

    def dequeueTail(self):
        if (self.head + 1) % self.size == self.tail:
            raise Exception('Queue underflow')

        x = self.q[self.tail]
        self.tail = (self.tail + self.size - 1) % self.size

        return x
        
