# LeetCode 1 - Two Sum

**Problem link**: [LeetCode 1](https://leetcode.com/problems/two-sum/)

---

## 🧠 Problem Summary

Given an array of integers `nums` and an integer `target`,  
return **indices of the two numbers** such that they add up to `target`.

You may assume that **each input would have exactly one solution**,  
and you **may not use the same element twice**.

You can return the answer in **any order**.

---

## ✅ Solutions

### ✔️ Solution 1: Brute-Force Method

- **Approach**:
  - Use nested loops to check every pair of elements in `nums`.
  - If the sum of a pair equals the `target`, return their indices.

- **Time Complexity**: `O(n^2)` — Two nested loops  
- **Space Complexity**: `O(1)` — No extra space used

---

### ✔️ Solution 2: Hashmap Method

- **Approach**:
  - Iterate through `nums` while maintaining a dictionary to store previously seen numbers and their indices.
  - For each number, calculate its complement as `target - num`.
  - If the complement exists in the dictionary, return both indices.
  - Otherwise, store the number and its index.

- **Time Complexity**: `O(n)` — One pass through the list  
- **Space Complexity**: `O(n)` — For storing elements in a dictionary

---

### 🔎 Example

```python
nums = [2, 7, 11, 15]
target = 9
Output: [0,1]
```
- Because nums[0] + nums[1] = 2 + 7 = 9, which is the target.