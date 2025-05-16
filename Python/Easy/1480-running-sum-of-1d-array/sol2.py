"""
Solution 2 for Leetcode 1480 - Running Sum of 1D Array

Approach:
- Iterating over the array while maintaining a cummulative sum.
- Appends the running sum to the result list at each step'

Time Complexity: O(n) - where n is the length of the input list
Space Complexity: O(n) - Where n is the length of the result list
"""


from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            running_sum.append(sum)
        return running_sum
    

if __name__ == "__main__":
    nums = [1,2,3,4] # test_case
    sol = Solution()
    print(sol.runningSum(nums))