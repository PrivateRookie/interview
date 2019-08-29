import unittest


def replace(s: str) -> str:
    return s.replace(" ", "02%")


class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(replace("ab d"), "ab02%d")

    def test_case2(self):
        self.assertEqual(replace("abc "), "abc02%")

    def test_case3(self):
        self.assertEqual(replace(" abc"), "02%abc")


if __name__ == "__main__":
    unittest.main()
