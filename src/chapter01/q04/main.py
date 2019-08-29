import unittest


def anagram(s: str, t: str) -> bool:
    return s == t[::-1]


class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(anagram("abcd", "dcba"), True)

    def test_case2(self):
        self.assertEqual(anagram("abcd", "dbca"), False)

    def test_case3(self):
        self.assertEqual(anagram("", ""), True)


if __name__ == "__main__":
    unittest.main()
