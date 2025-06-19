"""
✅ Solution for Leetcode 28 - Find the Index of the First Occurrence in a String

🔹 Approach:
- We are given two strings: `haystack` and `needle`.
- We want to find the index of the first occurrence of `needle` in `haystack`.
- If `needle` is not found, return -1.
- We iterate through `haystack`, slicing substrings of length equal to `needle`.
- At each step, check if the current substring equals `needle`.
- If yes, return the current index.
- If the loop ends without a match, return -1.

🔹 Time Complexity: O((N - M + 1) * M) → where N is length of `haystack`, M is length of `needle`
- Each comparison takes O(M), and we do this up to (N - M + 1) times in the worst case.
- In practice, for average strings with early mismatches, it's faster.

🔹 Space Complexity: O(1)
- No extra space used apart from variables (not counting input).
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(sol.strStr(haystack, needle)) # Output: 0