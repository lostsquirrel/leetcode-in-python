import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = set()
        if size < 3:
            return res
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return res
        for cursor in range(size):
            left = cursor + 1
            right = size - 1
            while left < right:
                mark = nums[cursor] + nums[left] + nums[right]
                if mark == 0:
                    res.add((nums[cursor], nums[left], nums[right]))
                    right -= 1
                elif mark > 0:
                    right -= 1
                else:
                    left += 1
        return res


class Test(unittest.TestCase):

    def test_case_1(self):
        self.validate([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])

    def test_case_2(self):
        self.validate([], [])

    def test_case_3(self):
        self.validate([0], [])

    def validate(self, nums: List[int], expected: List[List[int]]):
        s = Solution()
        self.assertEqual(expected, s.threeSum(nums))
