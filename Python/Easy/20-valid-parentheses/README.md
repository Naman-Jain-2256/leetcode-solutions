# LeetCode 20 - Valid Parentheses

**Problem link**: [LeetCode 20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

## 🧠 Problem Summary

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

---

## ✅ Solutions

### ✔️ Solution 1: 

- **Approach**:
  - Use a stack to track opening brackets.
    - Use a dictionary (`bracket_map`) to map closing to opening brackets.
    - Traverse the string:
        - If the character is an opening bracket, push it to the stack.
        - If it's a closing bracket:
            - Check if the stack is not empty and top matches the corresponding opening bracket.
            - If not, return False.
- After traversal, return `True` if the stack is empty (all brackets matched).

- **Time Complexity**: `O(n)` — `n` is the length of the string
- **Space Complexity**: `O(n)` —  Stack can hold all opening brackets

---

### 🔎 Example

```python
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False

Input: s = "([])"
Output: True

```