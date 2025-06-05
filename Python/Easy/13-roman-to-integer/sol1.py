"""
✅ Solution 1 for Leetcode 13 - Roman to Integer

Approach:
- Create a dictionary `roman_letters` mapping each Roman symbol to its integer value.
- Initialize a variable `num` to store the final result.
- Loop through the string `s` from index 0 to second-last character:
    - If the current Roman value is less than the next (e.g., I < V), subtract it from `num`.
    - Else, add the current value to `num`.
- Finally, add the value of the last character (since it has no "next" to compare with).

Time Complexity: O(n) - where 'n' is the length of the string
Space Complexity: O(1) - the dictionary size is constant
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        roman_letters = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Traverse through the string except the last character
        for i in range(len(s) - 1):
            if roman_letters[s[i]] < roman_letters[s[i + 1]]:
                num -= roman_letters[s[i]]
            else:
                num += roman_letters[s[i]]
        
        # Add the last character value
        return num + roman_letters[s[-1]]

# Driver code
if __name__ == '__main__':
    sol = Solution()
    s = 'MCMXCIV'  # Expected output: 1994
    print(sol.romanToInt(s))
