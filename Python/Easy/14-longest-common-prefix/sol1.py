from typing import List

"""
Solution 1 for Leetcode 14 - Longest Common Prefix

Approach:
- Start with the first string in the list as the reference.
- Iterate through each character of the first string.
- For each character, build a candidate prefix by appending one character at a time.
- Check if all strings in the list start with this candidate prefix using `startswith()`.
- If they do, update the common prefix.
- If any string doesn't match the candidate prefix, return the last valid prefix.

Time Complexity: O(N * M) - 
- N is the number of strings.
- M is the length of the shortest string (in the worst case, we compare each character of each string).

Space Complexity: O(1) - 
- No extra space used except a few variables (output string excluded).
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        res = ''
        if not strs:
            return ''
        for letter in strs[0]:
            res += letter
            for string in strs:
                if not string.startswith(res):
                    return common_prefix
            common_prefix = res
        return common_prefix
                

if __name__ == "__main__": 
    sol = Solution()
    strs = ["flower","flow","flight"]
    print(sol.longestCommonPrefix(strs))
