# LeetCode 9 - Palindrome Number

**Problem link**: [LeetCode 9 - Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

## 🧠 Problem Summary

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A **palindrome** is a number that reads the same backward as forward.

**Note**: Negative numbers are **not** palindromes.

---

## ✅ Solutions

### ✔️ Solution 1: Convert to String

- **Approach**:
  - Convert the number to a string.
  - Check if the string is equal to its reverse.

- **Time Complexity**: `O(n)` — where `n` is the number of digits  
- **Space Complexity**: `O(n)` — for the string and its reverse


---

### ✔️ Solution 2: Reverse The Integer

- **Approach**:
  - If the number is negative return `False`
  - Reverse th enumber using modulus `%` and floor division `//`
  - Compare the reversed number with the original.

- **Time Complexity**: `O(log₁₀(n))` — since we process each digit once
- **Space Complexity**: `O(1)` — No extra space used

---

### 🔎 Example

```python
Input: x = 121
Output: True
Explanation: Reads same forward and backward.

Input: x = -121
Output: False
Explanation: Reads 121- backward, not the same.

Input: x = 10
Output: False
Explanation: 10 reversed is 01.
```