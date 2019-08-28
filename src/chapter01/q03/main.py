import unittest


def remove_duplicates(s: str) -> str:
    if len(s) < 2:
        return s

    result = []
    for i in s:
        if i not in result:
            result.append(i)
    return "".join(result)


class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(remove_duplicates("abcd"), "abcd")

    def test_case2(self):
        self.assertEqual(remove_duplicates("aaaa"), "a")

    def test_case3(self):
        self.assertEqual(remove_duplicates(""), "")

    def test_case4(self):
        self.assertEqual(remove_duplicates("aabbcc"), "abc")


if __name__ == "__main__":
    unittest.main()
