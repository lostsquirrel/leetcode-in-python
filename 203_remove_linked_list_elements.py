import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(None, head)
        prev = dummy_head
        current = head
        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy_head.next


class Test(unittest.TestCase):

    def test_case01(self):
        self.validate([1, 2, 3, 4, 5], [1, 2, 6, 3, 4, 5, 6], 6)

    def test_case02(self):
        self.validate([], [7, 7, 7, 7], 7)

    def validate(self, expected: List[int], values: List[int], val: int):
        s = Solution()
        head = self.init_list(values)
        self.assertEqual(expected, self.reverse_list(s.removeElements(head, val)))

    @staticmethod
    def init_list(values: List[int]):
        dummy_head = ListNode()
        prev = dummy_head
        for x in values:
            prev.next = ListNode(x)
            prev = prev.next
        return dummy_head.next

    @staticmethod
    def reverse_list(head: ListNode):
        data = []
        c = head
        while c is not None:
            data.append(c.val)
            c = c.next

        return data
