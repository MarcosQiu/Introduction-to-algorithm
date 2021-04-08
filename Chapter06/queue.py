from min_priority_queue import MinPriorityQueue

class Queue:
	def __init__(self):
		self.priority_queue = MinPriorityQueue()
		self.key = 1

	def enqueue(self, val):
		"""
		Push an element into the queue.
		"""
		self.priority_queue.insert(val, self.key)
		self.key += 1

	def dequeue(self):
		"""
		Remove and return the element from the head of the queue.

		>>> q = Queue()
		>>> q.enqueue(1)
		>>> q.enqueue(2)
		>>> q.dequeue()
		1
		>>> q.dequeue()
		2
		"""
		return self.priority_queue.extract_min()

	def peek(self):
		"""
		Return the element from the head of the queue.

		>>> q = Queue()
		>>> q.enqueue(1)
		>>> q.enqueue(2)
		>>> q.peek()
		1
		"""
		return self.priority_queue.minimum()

	def is_empty(self):
		"""
		Check if the queue is empty.
		
		>>> q = Queue()
		>>> q.is_empty()
		True
		>>> q.enqueue(1)
		>>> q.is_empty()
		False
		"""
		return self.priority_queue.is_empty()
