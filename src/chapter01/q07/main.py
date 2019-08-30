from typing import List

import unittest

M = 10
N = 10


def set_zero(matrix: List[List[int]]) -> List[List[int]]:
    row, col = [], []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    for i in range(M):
        for j in range(N):
            if i in row or j in col:
                matrix[i][j] = 0
    return matrix


class TestCase(unittest.TestCase):
    def test_case1(self):
        source = [
            [9, 2, 5, 5, 2, 4, 1, 7, 1, 9],
            [8, 3, 2, 3, 4, 8, 3, 1, 2, 3],
            [2, 7, 5, 0, 9, 1, 1, 1, 7, 2],
            [3, 8, 4, 8, 6, 2, 2, 9, 5, 4],
            [9, 6, 3, 7, 4, 5, 1, 4, 6, 0],
            [6, 7, 1, 7, 7, 3, 7, 0, 7, 9],
            [1, 2, 7, 5, 6, 5, 6, 0, 3, 5],
            [7, 0, 2, 5, 9, 5, 5, 6, 6, 0],
            [4, 5, 1, 9, 4, 6, 9, 5, 4, 7],
            [2, 8, 2, 2, 9, 9, 9, 1, 6, 9],
        ]
        target = [
            [9, 0, 5, 0, 2, 4, 1, 0, 1, 0],
            [8, 0, 2, 0, 4, 8, 3, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 4, 0, 6, 2, 2, 0, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 1, 0, 4, 6, 9, 0, 4, 0],
            [2, 0, 2, 0, 9, 9, 9, 0, 6, 0],
        ]
        self.assertEqual(set_zero(source), target)


if __name__ == "__main__":
    unittest.main()
