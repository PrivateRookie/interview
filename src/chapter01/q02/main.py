import unittest

# NOTE use "!" to represent null


def reverse_str(s: str) -> str:
    # magic index !!!
    return s[-2::-1] + '!'


class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(reverse_str("abcd!"), "dcba!")

    def test_case2(self):
        self.assertEqual(reverse_str("!"), "!")


if __name__ == "__main__":
    unittest.main()
