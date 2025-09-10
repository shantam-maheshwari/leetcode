from typing import List

import pytest


class Solution:
    # approach 1
    # time complexity: O(n*n)
    # space complexity: O(n)
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     triplets = set()
    #     seen1 = set()

    #     for i, num1 in enumerate(nums):
    #         if num1 not in seen1:
    #             seen1.add(num1)
    #             target = -num1
    #             seen2 = set()
    #             for num2 in nums[i + 1 :]:
    #                 if target - num2 in seen2:
    #                     triplets.add(tuple(sorted((num1, num2, target - num2))))
    #                 seen2.add(num2)

    #     return list([list(t) for t in triplets])

    # approach 2
    # time complexity: O(n*log(n) + n*n)
    # space complexity: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i == 0 or nums[i] != nums[i - 1]:
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    if nums[left] + nums[right] < -nums[i]:
                        left += 1
                    elif nums[left] + nums[right] > -nums[i]:
                        right -= 1
                    else:
                        triplets.add((nums[i], nums[left], nums[right]))
                        j = left
                        while left < right and nums[j] == nums[left]:
                            left += 1
                        right -= 1
        return list(list(t) for t in triplets)


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_threeSum(nums: List[int], expected: List[List[int]]):
    result = Solution().threeSum(nums)
    result = set(tuple(sorted(triplet)) for triplet in result)

    expected = set(tuple(sorted(triplet)) for triplet in expected)

    assert result == expected
