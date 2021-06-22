import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return False
        if len(s) == 1:
            return False
        stack = []
        d = {'(': ')', '{': '}', '[': ']'}
        for _, c in enumerate(s):
            if c in d:
                stack.append(c)
            else:
                try:
                    if d[stack.pop()] != c:
                        return False
                except IndexError:
                    return False

        return False if stack else True


class TestValidParathenses(unittest.TestCase):
    def test_single(self):
        self.assertEqual(Solution().isValid("}"), False)
        self.assertEqual(Solution().isValid("{"), False)

    def test_inner(self):
        self.assertEqual(Solution().isValid("[{}]"), True)
        self.assertEqual(Solution().isValid("[{]"), False)

    def test_inrow(self):
        self.assertEqual(Solution().isValid("[]{}()"), True)
        self.assertEqual(Solution().isValid("[]{})"), False)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
