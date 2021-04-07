class MaxPriorityQueue:
	def __init__(self):
		self.heap = [0]

	def insert(self, el, key):
		inserted_idx = self.heap[0] + 1
		if inserted_idx < len(self.heap):
			self.heap[inserted_idx] = [key, el]
		else:
			self.heap.append([key, el])
		self.heap[0] += 1

		idx_to_check = inserted_idx
		while (
			idx_to_check > 1 and
			self.heap[idx_to_check][0] > self.heap[idx_to_check // 2][0]
		):
			self.heap[idx_to_check], self.heap[idx_to_check // 2] = self.heap[idx_to_check // 2], self.heap[idx_to_check]
			idx_to_check = idx_to_check // 2


	def maximum(self):
		assert self.heap[0] > 0, 'The priority queue is empty'
		return self.heap[1][1]

	def extract_max(self):
		assert self.heap[0] > 0, 'The priority queue is empty'
		self.heap[1], self.heap[self.heap[0]] = self.heap[self.heap[0]], self.heap[1]
		self.heap[0] -= 1

		idx_to_check = 1
		while idx_to_check * 2 <= self.heap[0]:
			max_idx = idx_to_check
			if self.heap[idx_to_check * 2][0] > self.heap[max_idx][0]:
				max_idx = idx_to_check * 2
			if (
				idx_to_check * 2 < self.heap[0] and
				self.heap[idx_to_check * 2 + 1][0] > self.heap[max_idx][0]
			):
				max_idx = idx_to_check * 2 + 1

			if max_idx == idx_to_check:
				break
			self.heap[idx_to_check], self.heap[max_idx] = self.heap[max_idx], self.heap[idx_to_check]
			idx_to_check = max_idx

		return self.heap[self.heap[0] + 1][1]



	def increase_key(self, idx, key):
		assert idx > 0 and idx <= self.heap[0], 'invalid idx'
		assert key > self.heap[idx][0], 'cannot decrease the key'

		self.heap[idx][0] = key
		idx_to_check = idx
		while (
			idx_to_check > 1 and
			self.heap[idx_to_check][0] > self.heap[idx_to_check // 2][0]
		):
			self.heap[idx_to_check], self.heap[idx_to_check // 2] = self.heap[idx_to_check // 2], self.heap[idx_to_check]
			idx_to_check = idx_to_check // 2