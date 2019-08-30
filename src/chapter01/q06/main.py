import unittest
from typing import List


def rotate(matrix: List[List[int]]) -> List[List[int]]:
    matrix[:] = map(list, zip(*matrix[::-1]))
    return matrix


class TestCase(unittest.TestCase):
    def setUp(self):
        self.matrix = []
        for i in range(1, 6):
            self.matrix.append(list(range(1+(i-1)*5, i*5+1)))

    def test_case1(self):
        target_matrix = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
        self.assertEqual(rotate(self.matrix), target_matrix)


if __name__ == "__main__":
    unittest.main()
