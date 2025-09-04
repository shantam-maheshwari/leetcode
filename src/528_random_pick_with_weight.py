import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        if not w:
            return

        self.prefix_sums = [w[0]]
        for i in range(1, len(w)):
            self.prefix_sums.append(self.prefix_sums[-1] + w[i])

    def pickIndex(self) -> int:
        if not self.prefix_sums:
            return -1

        total_sum = self.prefix_sums[-1]
        weight = random.randint(1, total_sum)

        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < weight:
                left = mid + 1
            else:
                right = mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
