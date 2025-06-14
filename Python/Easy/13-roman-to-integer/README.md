# LeetCode 13 - Roman to Integer

**Problem link**: [LeetCode 13 - Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

---

## 🧠 Problem Summary

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

---

## ✅ Solutions

### ✔️ Solution 1: 

- **Approach**:
- Create a dictionary `roman_letters` mapping each Roman symbol to its integer value.
- Initialize a variable `num` to store the final result.
- Loop through the string `s` from index 0 to second-last character:
    - If the current Roman value is less than the next (e.g., I < V), subtract it from `num`.
    - Else, add the current value to `num`.
- Finally, add the value of the last character (since it has no "next" to compare with).

- **Time Complexity**: `O(n)` — where `n` is the length of string
- **Space Complexity**: `O(1)` — the dictionary size is of constant size

---

### 🔎 Example

```python
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```