class FixSizeQueue:
    def __init__(self, size=10):
        self.size = size
        self.q = [None] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if (
            (self.head == 0 and self.tail == self.size - 1) or
            self.head == self.tail + 1
        ):
            raise Exception('Queue overflow')
        
        self.q[self.tail] = x
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.head == self.tail:
            raise Exception('Queue underflow')
        x = self.q[self.head]
        self.head = (self.head + 1) % self.size

        return x