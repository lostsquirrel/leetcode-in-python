import unittest
import logging
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = self.init_matrix(n)
        value = 1
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction_rank = 0
        max_value = n * n

        class Point:
            def __init__(self, x: int, y: int):
                self.x = x
                self.y = y

        class Boundary:
            def __init__(self, top: int, right: int, bottom: int, left: int):
                self.top = top
                self.right = right
                self.bottom = bottom
                self.left = left

        class Walker:
            def __init__(self):
                self.position = Point(0, 0)
                self.direction_rank: int = 0
                self.boundary = Boundary(0, n - 1, n - 1, 0)

            def walk(self):
                if self.reach_boundary():
                    self.direction_rank = (self.direction_rank + 1) % len(directions)
                    if self.direction_rank == 0:
                        self.boundary.top += 1
                    if self.direction_rank == 1:
                        self.boundary.right -= 1
                    if self.direction_rank == 2:
                        self.boundary.bottom -= 1
                    if self.direction_rank == 3:
                        self.boundary.left += 1
                direction = self.get_direction()
                logging.debug("{} {}".format(self.position.x, self.position.y))
                matrix[self.position.x][self.position.y] = value
                self.position.x += direction[0]
                self.position.y += direction[1]

            def reach_boundary(self) -> bool:
                if self.direction_rank == 0:
                    return self.position.y == self.boundary.right
                if self.direction_rank == 1:
                    return self.position.x == self.boundary.bottom
                if self.direction_rank == 2:
                    return self.position.y == self.boundary.left
                if self.direction_rank == 3:
                    return self.position.x == self.boundary.top

            def get_direction(self):
                return directions[self.direction_rank]

        w = Walker()
        while value <= max_value:
            w.walk()
            value += 1
        return matrix

    @staticmethod
    def init_matrix(n: int):
        return [[0 for i in range(n)] for i in range(n)]


class Test(unittest.TestCase):

    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def test_case01(self):
        self.validate(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_case02(self):
        self.validate(1, [[1]])

    def test_init(self):
        matrix = Solution.init_matrix(3)
        self.assertEqual(3, len(matrix))
        for row in matrix:
            self.assertEqual(3, len(row))

    def validate(self, n: int, expected: List[List[int]]):
        s = Solution()
        self.assertEqual(expected, s.generateMatrix(n))
