from typing import List

"""
Solution 2 for Leetcode 1672 - Richest Customer Wealth

Approach:
- Use a List Comprehension with max() to compute the wealth of each customer efficiently.

Time Complexity: O(m × n) - where 'm' is the number of customers and 'n' is the number of banks
Space Complexity: O(m) - as we are using List Comprehension for storing the sum of each customer’s wealth.
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if not accounts:
            return 0

        customer_wealths= [sum(wealth) for wealth in accounts]
        return max(customer_wealths)
    

if __name__ == "__main__":  # test_case run
    sol = Solution()
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    print(sol.maximumWealth(accounts)) # output: 6