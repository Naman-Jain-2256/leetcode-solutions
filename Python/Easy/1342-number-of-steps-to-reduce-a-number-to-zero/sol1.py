"""
Solution 1 for Leetcode 1342 - Number of Steps to Reduce a Number to Zero

Approach:
- Use a loop to repeatedly divide the number by 2 if it is even,
  or subtract 1 if it is odd.
- Count the number of operations until the number becomes zero.

Time Complexity: O(log n) - Each division by 2 reduces the number significantly
Space Complexity: O(1) - Only a constant number of variables used
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            count += 1
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
        return count
    
if __name__ == "__main__": # test_case run
    sol = Solution()
    num = 14
    print(sol.numberOfSteps(num)) # output: 6