from collections import defaultdict
import unittest


def unique_char_map(s: str) -> bool:
    char_map = defaultdict(int)
    for c in s:
        char_map[c] = char_map[c] + 1
    return all(c == 1 for c in char_map.values())


def unique_char_vec(string: str) -> bool:
    vec = [0 for _ in range(128)]
    unique = True
    for c in string:
        delta = ord(c)
        vec[delta] = vec[delta] + 1
        if vec[delta] > 1:
            unique = False
    return unique


class TestCase(unittest.TestCase):
    def test_unique_map(self):
        self.assertEqual(unique_char_map('abcd'), True)

    def test_not_unique_map(self):
        self.assertEqual(unique_char_map('aabdc'), False)

    def test_unique_vec(self):
        self.assertEqual(unique_char_vec('abcd'), True)

    def test_not_unique_vec(self):
        self.assertEqual(unique_char_vec('aabdc'), False)


if __name__ == '__main__':
    unittest.main()
