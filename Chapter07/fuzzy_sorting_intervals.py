import random

def find_intersection(nums, p, r):
    rand = random.choice(range(p, r + 1))
    nums[rand], nums[r] = nums[r], nums[rand]
    a = nums[r][0]
    b = nums[r][1]

    for i in range(p, r):
        if nums[i][0] <= b and nums[i][1] >= a:
            a = max(nums[i][0], a)
            b = min(nums[i][1], b)

    return (a, b)

def partition_left(nums, b, p, t):
    i = p - 1
    for j in range(p, t):
        if nums[j][1] < b:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[t] = nums[t], nums[i + 1]
    return i + 1

def partition_right(nums, a, p, r):
    i = p - 1
    for i in range(p, r):
        if nums[j][0] <= a:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[t] = nums[t], nums[i + 1]
    return i + 1

def fuzzy_sort(nums, p, r):
    if p < r:
        a, b = find_intersection(nums, p, r)
        t = partition_right(nums, a, p, r)
        q = partition_left(nums, b, p, t)
        fuzzy_sort(nums, p, q - 1)
        fuzzy_sort(nums, t + 1, r)
