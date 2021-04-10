import unittest
from numbers import Number
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            position = 0
        elif target > nums[-1]:
            position = len(nums)
        else:
            position = binary_search2(nums, target, 0, len(nums))
        return position


def binary_search(nums: List[int], target: int, start: int, end: int):
    if start == end:
        return end
    else:
        middle = (start + end) // 2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            return binary_search(nums, target, middle + 1, end)
        else:
            return binary_search(nums, target, 0, middle)


def binary_search2(nums: List[int], target: int, left: int, right: int):
    while left < right:
        middle = left + ((right - left) >> 1)
        if nums[middle] > target:
            right = middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return right


class SearchInsertPositionTest(unittest.TestCase):

    def test_case_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected = 2
        self.validator(expected, nums, target)

    def test_case_2(self):
        self.validator(1, [1, 3, 5, 6], 2)

    def test_case_3(self):
        self.validator(4, [1, 3, 5, 6], 7)

    def test_case_4(self):
        self.validator(0, [1, 3, 5, 6], 0)

    def test_case_5(self):
        self.validator(0, [1], 0)

    def test_case_6(self):
        self.validator(1, [1, 3], 2)

    def validator(self, expected, nums, target):
        s = Solution()
        result = s.searchInsert(nums, target)
        self.assertEqual(expected, result)
