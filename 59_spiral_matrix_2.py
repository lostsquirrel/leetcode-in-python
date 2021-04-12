import unittest
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = self.init_matrix(n)
        value = 1
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        direction_rank = 0

        class Point:
            def __init__(self, x: int, y: int):
                self.x = x
                self.y = y

        class Depth:
            def __init__(self, row: int, column: int):
                self.row = row
                self.column = column

        class Walker:
            def __init__(self):
                self.position = Point(0, 0)
                self.direction = directions[direction_rank]

            def walk(self, direction):
                self.position.x += direction[0]
                self.position.y += direction[1]

    @staticmethod
    def init_matrix(n: int):
        return [[0 for i in range(n)] for i in range(n)]


class Test(unittest.TestCase):

    def test_init(self):
        matrix = Solution.init_matrix(3)
        self.assertEqual(3, len(matrix))
        for row in matrix:
            self.assertEqual(3, len(row))

    def validate(self, n: int, expected: List[List[int]]):
        s = Solution()
        self.assertEqual(expected, s.generateMatrix(n))
