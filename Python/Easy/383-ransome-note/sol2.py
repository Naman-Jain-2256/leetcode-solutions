from collections import Counter

"""
Solution 2 for Leetcode 383 - Ransom Note

Approach:
- Use Python's built-in `Counter` from the `collections` module.
  - `Counter(ransomNote) - Counter(magazine)` will subtract the counts.
  - If the result is an empty Counter (i.e., no shortage of letters), return `True`; else, `False`.

Time Complexity: O(n + m) - where 'n' is length of ransomNote, 'm' is length of magazine
Space Complexity: O(1) - Because the alphabet size is constant (only lowercase letters)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
    
if __name__ == "__main__": # test_case run
    ransomNote = "ab"
    magazine = "ab"
    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine)) # output: False