class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = maxim = 0
        r = len(height) - 1

        while l != r and True:
            maxim = max(maxim, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxim
