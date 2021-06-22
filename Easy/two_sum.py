import unittest


class Solution:
    def twoSum(self, nums, target: int):
        dic = {}
        for ind, num in enumerate(nums):
            n = target - num
            if n not in dic:
                dic[num] = ind
            else:
                return [dic[n], ind]


class TestTwoSum(unittest.TestCase):
    def test_possible(self):
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])
        self.assertEqual(Solution().twoSum([0, 1], 1), [0, 1])

    def test_impossible(self):
        self.assertEqual(Solution().twoSum([1, 2, 3], 6), None)
        self.assertEqual(Solution().twoSum([3, 4], 6), None)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
