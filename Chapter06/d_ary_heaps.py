class DAryMaxHeaps:
    def __init__(self, d=5, arr=None):
        self.heap = arr or list()
        self.heap_size = len(self.heap)
        self.d = d
        self.neg_inf = -99999999
        self.inf = 99999999

        self.heapify()

    def is_empty(self):
        """
        Check if a d-ary heap is empty.

        >>> q = DAryMaxHeaps()
        >>> q.is_empty()
        True
        >>> q.insert(1, 10)
        >>> q.is_empty()
        False
        """
        return self.heap_size == 0

    def insert(self, el, key):
        """
        Insert a new el with key.
        """
        inserted_idx = self.heap_size
        if inserted_idx < len(self.heap):
            self.heap[inserted_idx] = [self.neg_inf, el]
        else:
            self.heap.append([self.neg_inf, el])
        self.heap_size += 1
        self.increase_key(inserted_idx, key)

    def maximum(self):
        """
        Return the element with maximum key.

        >>> q = DAryMaxHeaps()
        >>> q.insert(1, 10)
        >>> q.maximum()
        1
        >>> q.insert(2, 1)
        >>> q.maximum()
        1
        """
        assert self.heap_size > 0, 'The priority queue is empty'
        return self.heap[0][1]

    def extract_max(self):
        """
        Remove and return the element with maximum key.

        >>> q = DAryMaxHeaps()
        >>> q.insert(1, 10)
        >>> q.insert(2, 1)
        >>> q.extract_max()
        1
        >>> q.extract_max()
        2
        """
        assert self.heap_size > 0, 'The priority queue is empty'
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1
        self._max_heapify(0)

        return self.heap[self.heap_size][1]

    def heap_delete(self, idx):
        """
        Delete an element in position idx.

        >>> q = DAryMaxHeaps()
        >>> q.insert(1, 10)
        >>> q.insert(2, 1)
        >>> q.maximum()
        1
        >>> q.heap_delete(1)
        2
        """
        assert idx >= 0 and idx <= self.heap_size, 'invalid idx'
        self.increase_key(idx, self.inf)
        return self.extract_max()

    def increase_key(self, idx, key):
        """
        Increase the key of element in position idx.

        >>> q = DAryMaxHeaps()
        >>> q.insert(1, 10)
        >>> q.insert(2, 1)
        >>> q.maximum()
        1
        >>> q.increase_key(1, 20)
        >>> q.maximum()
        2
        """
        assert idx >= 0 and idx < self.heap_size, 'invalid idx'
        assert key > self.heap[idx][0], 'cannot decrease the key'

        idx_to_check = idx
        tmp = [key, self.heap[idx_to_check][1]]
        while idx_to_check > 0:
            parent = self._get_parent(idx_to_check)
            if self.heap[parent][0] < key:
                self.heap[idx_to_check] = self.heap[parent]
                idx_to_check = parent
            else:
                break
        self.heap[idx_to_check] = tmp

    def heapify(self):
        """
        >>> q = DAryMaxHeaps(arr=[[1, 10],[2, 11],[4, 12],[7, 13],[5, 14],[3, 15],[6, 16]])
        >>> q.extract_max()
        13
        >>> q.extract_max()
        16
        >>> q.extract_max()
        14
        >>> q.extract_max()
        12
        >>> q.extract_max()
        15
        >>> q.extract_max()
        11
        >>> q.extract_max()
        10
        """
        last_child_idx = self.heap_size - 1
        last_parent = self._get_parent(last_child_idx)
        for idx in range(last_parent, -1, -1):
            self._max_heapify(idx)

    def _get_parent(self, idx):
        if idx % self.d == 0:
            return idx // self.d - 1
        return idx // self.d

    def _max_heapify(self, idx):
        idx_to_check = idx
        while idx_to_check * self.d + 1 < self.heap_size:
            max_idx = idx_to_check
            child_idx = idx_to_check * self.d + 1
            while child_idx < self.heap_size and child_idx <= (idx_to_check + 1) * self.d:
                if self.heap[child_idx][0] > self.heap[max_idx][0]:
                    max_idx = child_idx
                child_idx += 1
            if max_idx != idx_to_check:
                self.heap[max_idx], self.heap[idx_to_check] = self.heap[idx_to_check], self.heap[max_idx]
                idx_to_check = max_idx
            else:
                break
        