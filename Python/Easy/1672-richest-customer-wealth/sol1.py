from typing import List

"""
Solution 1 for Leetcode 1672 - Richest Customer Wealth

Approach:
- Use a generator expression with max() to compute the wealth of each customer efficiently.

Time Complexity: O(m × n) - where 'm' is the number of customers and 'n' is the number of banks
Space Complexity: O(1) - constant extra space since we're using a generator
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)
    

if __name__ == "__main__":  # test_case run
    sol = Solution()
    accounts = [[1,2,3],[3,2,1]]
    print(sol.maximumWealth(accounts)) # output: 6