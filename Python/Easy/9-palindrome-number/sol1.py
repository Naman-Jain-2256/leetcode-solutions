"""
Solution 1 for Leetcode 9 - Palindrome Number

Approach:
- Convert int to string 
- Compare string with its reverse

Time Complexity: O(n) - 'n' is length of string 
Space Complexity: O(1) - No extra space used
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

if __name__ == "__main__":
    sol = Solution()
    x = -121
    print(sol.isPalindrome(x))  # Output: False
