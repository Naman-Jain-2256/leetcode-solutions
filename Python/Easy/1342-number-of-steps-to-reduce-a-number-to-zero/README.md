# LeetCode 1342 - Number of Steps to Reduce a Number to Zero

**Problem link**: [LeetCode 1342](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)

---

## 🧠 Problem Summary

Given an integer `num`, return the number of steps to reduce it to zero.

In one step:
- If the current number is **even**, divide it by `2`.
- If the current number is **odd**, subtract `1` from it.

---

## ✅ Solutions

### ✔️ Solution 1: Iterative Loop

- **Approach**:
  - Use a loop to repeatedly:
    - Divide by 2 if the number is even
    - Subtract 1 if the number is odd
  - Count the number of operations until the number becomes zero.

- **Time Complexity**: `O(log n)` — Dividing by 2 reduces the number exponentially.
- **Space Complexity**: `O(1)` — Constant space used.

---

## 🔎 Example:

**Input**:  
`num = 14`

**Output**:  
`6`

**Explanation**:  
Steps:  
14 → 7 → 6 → 3 → 2 → 1 → 0
