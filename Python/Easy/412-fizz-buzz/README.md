# LeetCode 412 - Fizz Buzz

**Problem link**: [LeetCode 412](https://leetcode.com/problems/fizz-buzz/)

---

## 🧠 Problem Summary

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by both `3` and `5`.
- `answer[i] == "Fizz"` if `i` is divisible by `3`.
- `answer[i] == "Buzz"` if `i` is divisible by `5`.
- `answer[i] == i` (as a string) if none of the above conditions are true.

---

## ✅ Solutions

### ✔️ Solution 1: List Comprehension

- **Approach**:  
  Use list comprehension to check:
  - `'FizzBuzz'` for numbers divisible by both 3 and 5 (`i % 15 == 0`)
  - `'Fizz'` for numbers divisible by 3
  - `'Buzz'` for numbers divisible by 5
  - Else, convert the number to a string.

- **Time Complexity**: `O(n)` — Iterate through numbers from `1` to `n`
- **Space Complexity**: `O(n)` — Output list of size `n`


### ✔️ Solution 2: For Loop

- **Approach**:
  Use for loop to check:
  - `'FizzBuzz'` for numbers divisible by both 3 and 5 (`i % 15 == 0`)
  - `'Fizz'` for numbers divisible by 3
  - `'Buzz'` for numbers divisible by 5
  - Else, convert the number to a string.
- **Time Complexity**: O(n) - where 'n' is the range of input
- **Space Complexity**: O(n) - where 'n' is the number of output list items
  
---

### 🔎 Example:

**Input**:  
`n = 20`

**Output**:  
```python
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
 '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz']
```