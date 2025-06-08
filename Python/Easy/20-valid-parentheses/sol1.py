"""
Solution 1 for Leetcode 20 - Valid Parentheses

Approach:
- Use a stack to track opening brackets.
- Use a dictionary (`bracket_map`) to map closing to opening brackets.
- Traverse the string:
    - If the character is an opening bracket, push it to the stack.
    - If it's a closing bracket:
        - Check if the stack is not empty and top matches the corresponding opening bracket.
        - If not, return False.
- After traversal, return True if the stack is empty (all brackets matched).

Time Complexity: O(n) - 'n' is the length of the string
Space Complexity: O(n) - Stack can hold all opening brackets
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                return False

        return not stack

if __name__ == "__main__":
    sol = Solution()
    s = "()[]{}"
    print(sol.isValid(s))