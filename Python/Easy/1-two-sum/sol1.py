from typing import List

"""
Solution 1 for Leetcode 1 - Two Sum

Approach:
- Brute-force method: Check every pair of elements in `nums`.
- If the sum of a pair equals the target, return their indices.

Time Complexity: O(n^2) - Two nested loops over the array
Space Complexity: O(1) - No extra space used
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Output: [0, 1]
