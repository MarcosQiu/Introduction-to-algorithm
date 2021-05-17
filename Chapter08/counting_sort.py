from collections import Counter

def counting_sort(arr, key_getter = lambda el: el):
    """
    >>> a = [[1, 3], [3, 1], [2, 2], [6, 1], [3, 2], [2, 1]]
    >>> counting_sort(a, key_getter=lambda a: a[0])
    [[1, 3], [2, 2], [2, 1], [3, 1], [3, 2], [6, 1]]
    """
    counter = Counter()
    max_key = 0
    for each in arr:
        max_key = max(max_key, key_getter(each))
        counter[key_getter(each)] += 1

    acc = list()
    total = 0
    for key in range(max_key + 1):
        total += counter[key]
        acc.append(total)

    result = [0] * total
    for idx in range(len(arr) - 1, -1, -1):
        idx_to_insert = acc[key_getter(arr[idx])] - 1
        result[idx_to_insert] = arr[idx]
        acc[key_getter(arr[idx])] -= 1
    
    return result
