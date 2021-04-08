class MinPriorityQueue:
	def __init__(self):
		self.heap = [0]
		self.inf = 9999999

	def is_empty(self):
		"""
		Check if a min-priority-queue is empty.

		>>> q = MinPriorityQueue()
		>>> q.is_empty()
		True
		>>> q.insert(1, 10)
		>>> q.is_empty()
		False
		"""
		return self.heap[0] == 0

	def insert(self, el, key):
		"""
		Insert a new el with key.
		"""
		inserted_idx = self.heap[0] + 1
		if inserted_idx < len(self.heap):
			self.heap[inserted_idx] = [self.inf, el]
		else:
			self.heap.append([self.inf, el])
		self.heap[0] += 1
		self.decrease_key(inserted_idx, key)

	def minimum(self):
		"""
		Return the element with minimum key.

		>>> q = MinPriorityQueue()
		>>> q.insert(1, 10)
		>>> q.minimum()
		1
		>>> q.insert(2, 1)
		>>> q.minimum()
		2
		"""
		assert self.heap[0] > 0, 'The priority queue is empty'
		return self.heap[1][1]

	def extract_min(self):
		"""
		Remove and return the element with minimum key.

		>>> q = MinPriorityQueue()
		>>> q.insert(1, 10)
		>>> q.insert(2, 1)
		>>> q.extract_min()
		2
		>>> q.extract_min()
		1
		"""
		assert self.heap[0] > 0, 'The priority queue is empty'
		self.heap[1], self.heap[self.heap[0]] = self.heap[self.heap[0]], self.heap[1]
		self.heap[0] -= 1

		idx_to_check = 1
		while idx_to_check * 2 <= self.heap[0]:
			min_idx = idx_to_check
			if self.heap[idx_to_check * 2][0] < self.heap[min_idx][0]:
				min_idx = idx_to_check * 2
			if (
				idx_to_check * 2 < self.heap[0] and
				self.heap[idx_to_check * 2 + 1][0] < self.heap[min_idx][0]
			):
				min_idx = idx_to_check * 2 + 1

			if min_idx == idx_to_check:
				break
			self.heap[idx_to_check], self.heap[min_idx] = self.heap[min_idx], self.heap[idx_to_check]
			idx_to_check = min_idx

		return self.heap[self.heap[0] + 1][1]


	def decrease_key(self, idx, key):
		"""
		Decrease the key of element in position idx.

		>>> q = MinPriorityQueue()
		>>> q.insert(1, 10)
		>>> q.insert(2, 1)
		>>> q.minimum()
		2
		>>> q.decrease_key(2, 0)
		>>> q.minimum()
		1
		"""
		assert idx > 0 and idx <= self.heap[0], 'invalid idx'
		assert key < self.heap[idx][0], 'cannot increase the key'

		idx_to_check = idx
		self.heap[idx_to_check][0] = key
		tmp = self.heap[idx_to_check]
		while (
			idx_to_check > 1 and
			key < self.heap[idx_to_check // 2][0]
		):
			self.heap[idx_to_check] = self.heap[idx_to_check // 2]
			idx_to_check = idx_to_check // 2
		self.heap[idx_to_check] = tmp
