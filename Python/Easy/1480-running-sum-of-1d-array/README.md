# LeetCode 1480 - Running Sum of 1D Array

**Problem link**: [LeetCode 1480](https://leetcode.com/problems/running-sum-of-1d-array/)

---

### 🧠 Problem Summary
Given an array `nums`, return an array `runningSum` where `runningSum[i] = sum(nums[0] ... nums[i])`.

---

## ✅ Solutions

### ✔️ Solution 1: In-Place Prefix Sum

- **Approach**: Modify the input list directly by updating each element as the running total.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **File**: `sol1.py`

---

### ✔️ Solution 2: Using Extra List

- **Approach**: Maintain a separate list to store the cumulative sum at each step.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **File**: `sol2.py`

