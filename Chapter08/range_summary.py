from collections import Counter

class RangeSummary:
    def __init__(self, arr):
        self.summary = Counter()
        self.max_num = 0
        for num in arr:
            self.summary[num] += 1
            self.max_num = max(self.max_num, num)

        for key in range(self.max_num + 1):
            self.summary[key] += self.summary[key - 1]

    def query(self, a, b):
        """
        >>> arr = [0] * 4 + [1] * 3 + [2] * 5 + [10] * 3
        >>> rs = RangeSummary(arr)
        >>> rs.query(2, 4)
        5
        >>> rs.query(10, 15)
        3
        >>> rs.query(-5, 12)
        15
        >>> rs.query(-5, 1)
        7
        """
        if b < 0 or a > self.max_num:
            return 0
        a = max(a, 0)
        b = min(b, self.max_num)
        return self.summary[b] - self.summary[a - 1]
