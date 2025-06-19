# Leetcode 28 - Find the Index of the First Occurrence in a String

**🔗 Problem link**: [Leetcode 28 - Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

---

## 🧠 Problem Summary

Given two strings `needle` and `haystack`, return the index of the **first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

---

## ✅ Solution

### ✔️ Sliding Window Approach

- **Approach**:
  - Let `n` be the length of `haystack`, and `m` be the length of `needle`.
  - If `m` is greater than `n`, return `-1` (needle can't fit in haystack).
  - Loop over `haystack` from index `0` to `n - m`.
  - At each index `i`, compare the substring `haystack[i:i+m]` with `needle`.
  - If they match, return `i`.
  - If the loop completes without a match, return `-1`.

- **Time Complexity**: `O(n * m)` in the worst case  
  - Where `n` is the length of `haystack` and `m` is the length of `needle`.

- **Space Complexity**: `O(1)`  
  - No extra space used.

---

## 🔎 Examples

```python
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1
