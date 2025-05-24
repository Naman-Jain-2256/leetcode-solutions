# LeetCode 1672 - Richest Customer Wealth

**Problem link**: [LeetCode 1672](https://leetcode.com/problems/richest-customer-wealth/)

## 🧠 Problem Summary

You are given a 2D list `accounts` where `accounts[i][j]` is the amount of money the `i`ᵗʰ customer has in the `j`ᵗʰ bank.  
Return the **wealth** that the richest customer has.

A customer's **wealth** is the sum of money in all their bank accounts.  
The richest customer is the one with the maximum wealth.

---

## ✅ Solutions

### ✔️ Solution 1: Generator Expression + `max()`

- **Approach**: Use a generator expression to calculate the sum of each customer's accounts and return the maximum.
- **Time Complexity**: O(m × n), where `m` = number of customers and `n` = number of banks
- **Space Complexity**: O(1) — constant space with generator
- **File**: `sol1.py`


## ✔️ Solution 1: List Comprehension + `max()`

- **Approach**: Use a generator expression to calculate the sum of each customer's accounts and return the maximum.
- **Time Complexity**: O(m × n), where `m` = number of customers and `n` = number of banks
- **Space Complexity**: O(m) — as we are using List Comprehension for storing the sum of each customer’s wealth.
- **File**: `sol2.py`



> Example:  
> `accounts = [[1, 2, 3], [3, 2, 1]]`  
> Output: `6`  
> (Customer 0 has 6, Customer 1 has 6 → max = 6)