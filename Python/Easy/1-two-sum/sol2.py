from typing import List

"""
Solution 2 for Leetcode 1 - Two Sum

Approach:
- Hashmap Method:
  - Iterate over each element in the list.
  - For each element, check if (target - current number) is already in the hashmap.
  - If it is, return the indices.
  - Otherwise, store the current number with its index in the hashmap.

Time Complexity: O(n) - One pass through the list
Space Complexity: O(n) - Storing elements in a dictionary
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], index]
            hashmap[num] = index

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Output: [0, 1]
