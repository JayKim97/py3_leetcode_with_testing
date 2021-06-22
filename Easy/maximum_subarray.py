# https://leetcode.com/problems/maximum-subarray/
import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0]]
        maxim = nums[0]
        for i in range(1, len(nums)):
            dp.append(nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0))
            maxim = max(maxim, dp[i])
        return maxim


class TestMaxSub(unittest.TestCase):
    def test_single(self):
        self.assertEqual(Solution().maxSubArray([1]), 1)

    def test_max_sub(self):
        self.assertEqual(Solution().maxSubArray(
            [-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_repeating(self):
        self.assertEqual(Solution().maxSubArray([1, -1, 1, -1, 1, -1]), 1)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
