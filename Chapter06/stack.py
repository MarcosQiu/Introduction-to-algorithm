from max_priority_queue import MaxPriorityQueue

class Stack:
	def __init__(self):
		self.priority_queue = MaxPriorityQueue()
		self.key = 1

	def push(self, val):
		"""
		Push an element into the stack.
		"""
		self.priority_queue.insert(val, self.key)
		self.key += 1

	def pop(self):
		"""
		Remove and return the element from the top of the stack.

		>>> s = Stack()
		>>> s.push(1)
		>>> s.push(2)
		>>> s.pop()
		2
		>>> s.pop()
		1
		"""
		return self.priority_queue.extract_max()

	def peek(self):
		"""
		Return the element from the top of the stack.

		>>> s = Stack()
		>>> s.push(1)
		>>> s.push(2)
		>>> s.peek()
		2
		"""
		return self.priority_queue.maximum()

	def is_empty(self):
		"""
		Check if the stack is empty.
		
		>>> s = Stack()
		>>> s.is_empty()
		True
		>>> s.push(1)
		>>> s.is_empty()
		False
		"""
		return self.priority_queue.is_empty()
