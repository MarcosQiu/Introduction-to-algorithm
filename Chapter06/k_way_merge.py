from min_priority_queue import MinPriorityQueue

def k_way_merge(lists, k):
	"""
	k-way merge sorted lists in O(nlogk) time.

	>>> k_way_merge([[1,2,5,9],[2,4,12],[13]], 3)
	[1, 2, 2, 4, 5, 9, 12, 13]
	"""
	indexes = [1] * k
	priority_queue = MinPriorityQueue()

	for i in range(k):
		# i indicates which list this is from
		priority_queue.insert([i, lists[i][0]], lists[i][0])

	merged_result = list()
	while not priority_queue.is_empty():
		idx, val = priority_queue.extract_min()
		merged_result.append(val)
		# if that list is not empty yet
		if indexes[idx] < len(lists[idx]):
			value = lists[idx][indexes[idx]]
			priority_queue.insert([idx, value], value)
			indexes[idx] += 1

	return merged_result
