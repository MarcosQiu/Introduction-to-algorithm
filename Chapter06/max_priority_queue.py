class MaxPriorityQueue:
	def __init__(self):
		self.heap = [0]
		self.neg_inf = -9999999

	def is_empty(self):
		"""
		Check if a min-priority-queue is empty.

		>>> q = MaxPriorityQueue()
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
			self.heap[inserted_idx] = [self.neg_inf, el]
		else:
			self.heap.append([self.neg_inf, el])
		self.heap[0] += 1
		self.increase_key(inserted_idx, key)

	def maximum(self):
		"""
		Return the element with maximum key.

		>>> q = MaxPriorityQueue()
		>>> q.insert(1, 10)
		>>> q.maximum()
		1
		>>> q.insert(2, 1)
		>>> q.maximum()
		1
		"""
		assert self.heap[0] > 0, 'The priority queue is empty'
		return self.heap[1][1]

	def extract_max(self):
		"""
		Remove and return the element with maximum key.

		>>> q = MaxPriorityQueue()
		>>> q.insert(1, 10)
		>>> q.insert(2, 1)
		>>> q.extract_max()
		1
		>>> q.extract_max()
		2
		"""
		assert self.heap[0] > 0, 'The priority queue is empty'
		self.heap[1], self.heap[self.heap[0]] = self.heap[self.heap[0]], self.heap[1]
		self.heap[0] -= 1
		self._max_heapify(1)

		return self.heap[self.heap[0] + 1][1]

	def heap_delete(self, idx):
		"""
		Delete an element in position idx.

		>>> q = MaxPriorityQueue()
		>>> q.insert(1, 10)
		>>> q.insert(2, 1)
		>>> q.maximum()
		1
		>>> q.heap_delete(2)
		2
		"""
		assert idx > 0 and idx <= self.heap[0], 'invalid idx'
		el_to_return = self.heap[idx][1]
		old_key = self.heap[idx][0]
		self.heap[idx] = self.heap[self.heap[0]]			
		if old_key < self.heap[self.heap[0]][0]:
			self.increase_key(idx, self.heap[idx][0])
		else:
			self._max_heapify(idx)
		self.heap[0] -= 1

		return el_to_return

	def increase_key(self, idx, key):
		"""
		Increase the key of element in position idx.

		>>> q = MaxPriorityQueue()
		>>> q.insert(1, 10)
		>>> q.insert(2, 1)
		>>> q.maximum()
		1
		>>> q.increase_key(2, 20)
		>>> q.maximum()
		2
		"""
		assert idx > 0 and idx <= self.heap[0], 'invalid idx'
		assert key > self.heap[idx][0], 'cannot decrease the key'

		idx_to_check = idx
		self.heap[idx_to_check][0] = key
		tmp = self.heap[idx_to_check]
		while (
			idx_to_check > 1 and
			key > self.heap[idx_to_check // 2][0]
		):
			self.heap[idx_to_check] = self.heap[idx_to_check // 2]
			idx_to_check = idx_to_check // 2
		self.heap[idx_to_check] = tmp

	def _max_heapify(self, idx):
		while idx * 2 <= self.heap[0]:
			max_idx = idx
			if self.heap[idx * 2][0] > self.heap[max_idx][0]:
				max_idx = idx * 2
			if (
				idx * 2 < self.heap[0] and
				self.heap[idx * 2 + 1][0] > self.heap[max_idx][0]
			):
				max_idx = idx * 2 + 1

			if max_idx == idx:
				break
			self.heap[idx], self.heap[max_idx] = self.heap[max_idx], self.heap[idx]
			idx = max_idx