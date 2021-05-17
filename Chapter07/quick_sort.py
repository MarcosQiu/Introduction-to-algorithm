import random

def sort(nums):
    improved_quicksort(nums, 0, len(nums) - 1)

def quick_sort(nums, p, r):
    if p < r:
        pivot = partition(nums, p, r)
        quick_sort(nums, p, pivot - 1)
        quick_sort(nums, pivot + 1, r)


def partition(nums, p, r, rand_pick = True):
    """
    >>> a = [1,3,5,2,3,4,7]
    >>> partition(a, 0, len(a) - 1, False)
    6
    >>> a = [1,3,5,2,3,4,3]
    >>> partition(a, 0, len(a) - 1, False)
    4
    >>> a = [1,1,1,1,1]
    >>> partition(a, 0, len(a) - 1, False)
    4
    """
    if rand_pick:
        rand_idx = random.choice(range(p, r + 1))
        nums[rand_idx], nums[r] = nums[r], nums[rand_idx]
    pivot = nums[r]

    i = p - 1
    for j in range(p, r):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1

def improved_quicksort(nums, p, r):
    if p < r:
        q, t = improved_partition(nums, p, r)
        improved_quicksort(nums, p, q - 1)
        improved_quicksort(nums, t + 1, r)

def improved_partition(nums, p, r, rand_pick = True):
    """
    >>> a = [7,3,5,2,3,4,1]
    >>> q, t = improved_partition(a, 0, len(a) - 1, False)
    >>> q
    6
    >>> t
    6
    >>> a = [3,3,5,2,3,4,1]
    >>> q, t = improved_partition(a, 0, len(a) - 1, False)
    >>> q
    2
    >>> t
    4
    >>> a = [1,1,1,1,1]
    >>> q, t = improved_partition(a, 0, len(a) - 1, False)
    >>> q
    0
    >>> t
    4
    """
    if rand_pick:
        rand_idx = random.choice(range(p, r + 1))
        nums[rand_idx], nums[p] = nums[p], nums[rand_idx]
    pivot = nums[p]

    low = high = p
    for j in range(p + 1, r + 1):
        if nums[j] < pivot:
            y = nums[j]
            nums[high + 1] = nums[low]
            nums[low] = y
            low = low + 1
            high = high + 1
        elif nums[j] == pivot:
            nums[high + 1], nums[j] = nums[j], nums[high + 1]
            high += 1
    
    return (low, high)

def tail_recursive_quicksort(nums, p, r):
    while p < r:
        q = partition(nums, p, r)
        tail_recursive_quicksort(nums, p, q - 1)
        p = q + 1
