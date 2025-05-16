"""
Solution 1 for Leetcode 1480 - Running Sum of 1D Array

Approach:
- Iterate through the array starting from index 1.
- For each index `i`, updates `nums[i]` to be the sum of `nums[i]` and `nums[i-1]`.
- This transforms the list-in place into the running sum.

Time Complexity: O(n) - where n is the length of the input list
Space Complexity: O(1) - no extra space is used, modifies input list in-place
"""
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
        
if __name__ == '__main__':  # test_case run
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.runningSum(nums)) # output [1,3,6,10]