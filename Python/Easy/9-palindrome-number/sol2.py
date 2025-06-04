"""
Solution 2 for Leetcode 9 - Palindrome Number

Approach:
- Reverse the number using modulus and floor division.

Time Complexity: O(log₁₀(n)) - where n is the input number (number of digits in base 10)
Space Complexity: O(1) - No extra space used
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = 0
        original = x

        while x > 0:
            reversed_num = (reversed_num*10) + (x % 10)
            x //= 10

        return original == reversed_num

if __name__ == "__main__":
    sol = Solution()
    x = -121
    print(sol.isPalindrome(x)) # Output: False