from typing import List

"""
Solution 1 for Leetcode 14 - Longest Common Prefix

Approach:
- If the input list is empty, return an empty string.
- Use the first string in the list as the reference word.
- Iterate over each character (with index) in the first word.
- For every other word in the list, check:
    - If the current index exceeds the length of the word (which means the word is shorter), or
    - If the character at this index in the word is different from the current character in the reference.
    - If any mismatch is found, return the prefix built so far.
- If all characters at the current index match, append the character to the prefix.
- After all iterations, return the full prefix.

Time Complexity: O(N × M)  
- N = number of strings  
- M = length of the shortest string (in worst case we compare that many characters for each string)

Space Complexity: O(1)  
- Only uses a few variables for tracking and does not require extra space (excluding output string).
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        prefix = ''
        for index, letter in enumerate(strs[0]):
            for word in strs:
                if index >= len(word) or word[index] != letter:
                    return prefix
            prefix += letter
        return prefix

if __name__ == "__main__": 
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))  # Output: "fl"
