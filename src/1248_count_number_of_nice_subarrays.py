from typing import List

import pytest

# # time: O(n^2), space: O(1)
# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         result = 0

#         for i in range(len(nums)):
#             odd = 0
#             for j in range(i, len(nums)):
#                 if nums[j] % 2 == 1:
#                     odd += 1
#                 if odd == k:
#                     result += 1

#         return result


# # time: O(n), space: O(n)
# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         # odd_0_to_a + odd_a_to_b = curr_odd
#         # => odd_0_to_a + k = curr_odd
#         # => odd_0_to_a = curr_odd - k

#         # At each 'b', count the number of 'a' such that odd_0_to_a = curr_odd - k

#         result = 0

#         odd_counter = {0: 1}  # how many prefixes have `key` number of odd numbers
#         curr_odd = 0
#         for num in nums:
#             if num % 2 == 1:
#                 curr_odd += 1

#             result += odd_counter.get(curr_odd - k, 0)

#             odd_counter[curr_odd] = odd_counter.get(curr_odd, 0) + 1

#         return result


# sliding window
# time: O(n), space: O(1)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        left = right = 0
        count = 0
        while right < len(nums):
            if nums[right] % 2 == 1:
                k -= 1
                count = 0

            while k == 0:
                count += 1
                if nums[left] % 2 == 1:
                    k += 1
                left += 1

            result += count
            right += 1

        return result


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([1, 1, 2, 1, 1], 3, 2),
        ([2, 4, 6], 1, 0),
        ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2, 16),
    ],
)
def test_numberOfSubarrays(nums: List[int], k: int, expected: int):
    assert Solution().numberOfSubarrays(nums, k) == expected
