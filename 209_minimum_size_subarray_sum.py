import unittest
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub_sum = 0
        left = 0
        size = len(nums)
        res = size + 1
        for right in range(size):
            sub_sum += nums[right]
            while sub_sum >= target:
                sub_length = (right - left + 1)
                if sub_length < res:
                    res = sub_length
                sub_sum -= nums[left]
                left += 1
        if res == (size + 1):
            return 0
        else:
            return res


class Test(unittest.TestCase):

    def test_case01(self):
        self.validator(7, [2, 3, 1, 2, 4, 3], 2)

    def test_case02(self):
        self.validator(4, [1, 4, 4], 1)

    def test_case03(self):
        self.validator(11, [1, 1, 1, 1, 1, 1, 1, 1], 0)

    def validator(self, target: int, nums: List[int], expected: int):
        s = Solution()
        self.assertEqual(expected, s.minSubArrayLen(target, nums))
