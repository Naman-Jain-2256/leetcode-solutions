# LeetCode 14 - Longest Common Prefix

**🔗 Problem link**: [LeetCode 14 - Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

---

## 🧠 Problem Summary

Write a function to find the **longest common prefix** string amongst an array of strings.

If there is **no common prefix**, return an **empty string `""`**.

---

## ✅ Solution

### ✔️ Solution 1: Brute-Force Character-by-Character Comparison

- **Approach**:
    - Use the first string as the reference.
    - Iterate through each character of the first string (indexed).
    - For each character, check if it matches the character at the same index in every other string.
    - If all strings have the same character at that index, add it to the prefix.
    - If any mismatch is found or a string is too short, return the prefix found so far.

- **Time Complexity**: `O(N * M)`  
  - `N` = number of strings.  
  - `M` = length of the shortest string (we may compare each character across all strings).

- **Space Complexity**: `O(1)`  
  - Only a few variables used for tracking the prefix.  
  - No extra data structures are required (excluding output).

---

### ✔️ Solution 2: Brute-Force Method (Slightly Optimized)

- **Approach**:
  - If the input list is empty, return an empty string.
  - Use the first string in the list as the reference word.
  - Iterate over each character (with index) in the first word.
  - For every other word in the list, check:
      - If the current index exceeds the length of the word, or
      - If the character at this index in the word is different.
      - If any mismatch is found, return the prefix built so far.
  - If all characters at the current index match, append the character to the prefix.
  - After all iterations, return the full prefix.

- **Time Complexity**: `O(N * M)`  
  - `N` = number of strings.  
  - `M` = length of the shortest string (we may compare each character across all strings).

- **Space Complexity**: `O(1)`  
  - Only a few variables used for tracking the prefix.  
  - No extra data structures are required (excluding output).

---

### 🔎 Example

```python
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```