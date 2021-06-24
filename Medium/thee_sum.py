from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = nums[j + 1:]
                target = (nums[i] + nums[j]) * -1
                search = self.binarySearch(temp, 0, len(temp) - 1, target)
                if search >= 0:
                    result = [nums[i], nums[j], target]
                    if result not in res:
                        res.append([nums[i], nums[j], target])
        return res

    def binarySearch(self, arr, l, r, x):
        if r >= l:
            mid = (r - l) // 2 + l
            if (arr[mid] == x):
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid - 1, x)
            return self.binarySearch(arr, mid + 1, r, x)
        return -1


arr = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(arr))
