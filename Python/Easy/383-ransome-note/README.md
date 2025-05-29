# LeetCode 383 - Ransom Note

**Problem link**: [LeetCode 383](https://leetcode.com/problems/ransom-note/)

---

## 🧠 Problem Summary

Given two strings `ransomNote` and `magazine`,  
return `true` if `ransomNote` can be constructed by using the letters from  
`magazine`, and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

---

## ✅ Solutions

### ✔️ Solution 1: Using Hashmaps and For Loop

- **Approach**:
  - Use two dictionaries (hashmaps) to count the frequency of each character 
    in `ransomNote` and `magazine`.
  - Then, for each character in `ransomNote`, check if `magazine` has enough of it.

- **Time Complexity**: `O(n + m)` — where `n` is the length of `ransomNote`, `m` is the length of `magazine`  
- **Space Complexity**: `O(1)` — because the alphabet size is constant (only lowercase English letters)

## 🔎 Example

```python
ransomNote = "aa"
magazine = "ab"
```
Output: `False`

---

### ✔️ Solution 2: Using `collections.Counter`

- **Approach**:
  - Use Python's built-in `Counter` from the `collections` module.
  - `Counter(ransomNote) - Counter(magazine)` will subtract the counts.
  - If the result is an empty Counter (i.e., no shortage of letters), return `True`; else, `False`.

- **Time Complexity**: `O(n + m)` — where `n` is the length of `ransomNote`, `m` is the length of `magazine`  
- **Space Complexity**: `O(1)` — because the alphabet size is constant (only lowercase English letters)

---

### 🔎 Example:

```python
from collections import Counter

ransomNote = "aa"
magazine = "ab"

Counter(ransomNote)  # {'a': 2}
Counter(magazine)    # {'a': 1, 'b': 1}

Counter(ransomNote) - Counter(magazine)  # {'a': 1} → not empty, so return False
```
Output: `False`