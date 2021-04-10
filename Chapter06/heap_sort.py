def max_heapify(A, i):
	while i * 2 <= A[0]:
		max_idx = i
		if A[i * 2] > A[max_idx]:
			max_idx = i * 2
		if i * 2 + 1 <= A[0] and A[i * 2 + 1] > A[max_idx]:
			max_idx = i * 2 + 1
		if max_idx == i:
			break
		A[i], A[max_idx] = A[max_idx], A[i]
		i = max_idx

def heapify(A):
	for idx in range(A[0] // 2, 0, -1):
		max_heapify(A, idx)

def heap_sort(nums):
	"""
	Sort an array with heap sort. The first number
	in the array should be the size of the list.

	>>> nums = [8, 4, 2, 9, 10, 1, 5, 2, 9]
	>>> heap_sort(nums)
	>>> nums
	[0, 1, 2, 2, 4, 5, 9, 9, 10]
	"""
	heapify(nums)
	while nums[0] > 0:
		nums[1], nums[nums[0]] = nums[nums[0]], nums[1]
		nums[0] -= 1
		max_heapify(nums, 1)