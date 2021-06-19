def in_place_counting_sort(A, key_getter = lambda el: el):
    """
    >>> a = [[1, 3], [3, 1], [2, 2], [6, 1], [3, 2], [2, 1]]
    >>> in_place_counting_sort(a, key_getter=lambda a: a[0])
    >>> a
    [[1, 3], [2, 1], [2, 2], [3, 2], [3, 1], [6, 1]]
    >>> a = [1,4,2,7,4,3]
    >>> in_place_counting_sort(a)
    >>> a
    [1, 2, 3, 4, 4, 7]
    """
    max_key = 0
    for each in A:
        max_key = max(max_key, key_getter(each))

    C = [0] * (max_key + 1)
    for j in range(len(A)):
        C[key_getter(A[j])] += 1
    C[0] = [0, C[0]  - 1]
    for i in range(1, max_key + 1):
        C[i] = [C[i - 1][1] + 1, C[i] + C[i - 1][1]]

    for i in range(len(A)):
        key = key_getter(A[i])
        if (i <= C[key][1] or (key != max_key and i >= C[key + 1][0])):
            el_to_insert = A[i]
            A[i] = None
            while True:
                insert_idx = C[key_getter(el_to_insert)][1] - 1
                C[key_getter(el_to_insert)][1] -= 1
                el_to_insert, A[insert_idx] = A[insert_idx], el_to_insert
                if el_to_insert is None:
                    break